#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;








#include <deque>
#include <vector>

// Un graphe est un tableau de noeuds dont chacun contient la liste des liens vers ses voisins.
// Un lien contient un noeud (le voisin) et son coût de trajet.

// Fonctions nécessaires de la classe Graphe :
//		unsigned int size() const;
//		const Noeud& operator[](unsigned int index) const;

// Fonctions nécessaires de la classe Noeud :
//		unsigned int getIndex() const;
//		const std::vector<Lien*>& getLinks() const;
//			Note :	std::vector peut être remplacé par tout autre conteneur de List* pouvant être itéré.
// Fonctions supplémentaires nécessaires pour l'algorithme A* :
//		bool isFinal() const;
//		unsigned int getHeuristic() const;
//			Note :	Cette fonction doit renvoyer la distance minimale estimée du noeud jusqu'à un noeud final.
//					Afin que l'algorithme fourni ici fonctionne, cette fonction doit vérifier :
//						Pour tous noeuds x et y : h(x) <= h(y) + d(x, y).
//					La classe fournie par défaut ici implémente une heuristique nulle :
//					son utilisation revient à effectuer l'algorithme de Dijkstra sur le graphe fourni.

// Fonctions nécessaires de la classe Lien :
//		unsigned int getCost() const;
//		unsigned int getTargetIndex() const;



// Implémentation minimale de ces classes
class Graph;
class Link
{
protected:
	unsigned int fromIndex;
	unsigned int targetIndex;
	unsigned int cost;

public:
	unsigned int getFromIndex() const	{ return fromIndex; }
	unsigned int getTargetIndex() const	{ return targetIndex; }
	unsigned int getCost() const		{ return cost; }

	Link(unsigned int _fromIndex, unsigned int _targetIndex, unsigned int _cost)
		: fromIndex(_fromIndex), targetIndex(_targetIndex), cost(_cost) { }
};
class Node
{
	friend Graph;

protected:
	unsigned int index;
	std::vector<Link> links;

	bool finalNode;
	unsigned int heuristic;

public:
	unsigned int getIndex() const				{ return index; }
	const std::vector<Link>& getLinks() const	{ return links; }

	bool isFinal() const						{ return finalNode; }
	unsigned int getHeuristic() const			{ return heuristic; }

	Node(unsigned int _index)
		: index(_index), finalNode(false), heuristic((unsigned int)(-1))	{ }
};
class Graph
{
protected:
	std::vector<Node> nodes;

public:
	Graph(unsigned int nodesNb)
	{
		nodes.reserve(nodesNb);
		for (unsigned int i = 0; i < nodesNb; i++)
			nodes.push_back(Node(i));
	}

	void addLink(unsigned int start, unsigned int end, unsigned int cost, bool oneDirection = false)
	{
		nodes[start].links.push_back(Link(start, end, cost));
		if (!oneDirection)
			nodes[end].links.push_back(Link(end, start, cost));
	}
	void removeLink(unsigned int start, unsigned int end, bool oneDirection = false, bool costCheck = false, unsigned int cost = 0)
	{
		// Si costCheck == true : tous les liens de start à end sont supprimés, peu importe leur coût ;
		// sinon on ne supprime que les liens de start à end avec le coût spécifié.
		{
			auto& links = nodes[start].links;
			for (auto it = links.begin(); it != links.end(); ++it)
				if (it->getTargetIndex() == end && (!costCheck || it->getCost() == cost))
					links.erase(it);
		}

		if (!oneDirection)
		{
			auto& links = nodes[end].links;
			for (auto it = links.begin(); it != links.end(); ++it)
				if (it->getTargetIndex() == start && (!costCheck || it->getCost() == cost))
					links.erase(it);
		}
	}

	void setNodeFinal(unsigned int node, bool isFinal = true)
	{
		nodes[node].finalNode = isFinal;
	}
	void setNodeHeuristic(unsigned int node, unsigned int heuristic)
	{
		nodes[node].heuristic = heuristic;
	}

	void addNodes(int nbOfnodesToAdd = 1)
	{
		nodes.reserve(nodes.size() + nbOfnodesToAdd);
		for (int i = 0; i < nbOfnodesToAdd; i++)
			nodes.push_back(Node(nodes.size()));
	}

	unsigned int size() const
	{
		return nodes.size();
	}
	Node& operator[](unsigned int index)
	{
		return nodes[index];
	}
	const Node& operator[](unsigned int index) const
	{
		return nodes[index];
	}
};

// Algorithme de Dijkstra : parcours tout le graphe depuis un point de départ et détermine tous les chemins les plus courts depuis ce point
template<class Graphe = Graph, class Noeud = Node, class Lien = Link>
class Dijkstra
{
protected:
	struct DjNodeInfo
	{
		unsigned int previousNode;
		unsigned int totalCost;
		bool alreadyVisited;

		DjNodeInfo() : previousNode((unsigned int)(-1)), totalCost((unsigned int)(-1))
			, alreadyVisited(false)
		{ }
	};

	const Graphe& g;
	std::vector<DjNodeInfo> dj;

public:
	Dijkstra(const Graphe& gr) : g(gr) { }

	void computeShortestPathsFrom(unsigned int startNode);

	bool canReachNode(unsigned int node) const;
	unsigned int getCostTo(unsigned int node) const;
	std::deque<unsigned int> getShortestPathTo(unsigned int endNode) const;
};







int swap(int i)
{
	deque<int> digits;
	while (i > 0)
	{
		digits.push_back(i % 10);
		i /= 10;
	}

	int k = 0;
	while (!digits.empty())
	{
		int d = digits[0];
		k = k * 10 + d;
		digits.pop_front();
	}
	return k;
}
int main()
{

	int nbTests;
	cin >> nbTests;
	vector<int> ns;
	for (int testId = 0; testId < nbTests; testId++)
	{
		int N;
		cin >> N;
		ns.push_back(N);
	}

	int N = *max_element(ns.begin(), ns.end());

	Graph g(N + 1);
	Dijkstra<> dj(g);
	for (int i = 0; i < N + 1; i++)
	{
		// i -> i+1
		if (i < N)
			g.addLink(i, i + 1, 1, true);

		int sw = swap(i);
		if (sw <= N)
			g.addLink(i, sw, 1, true);
	}
	dj.computeShortestPathsFrom(1);

	for (int testId = 0; testId < nbTests; testId++)
		cout << "Case #" << testId + 1 << ": " << dj.getCostTo(ns[testId]) + 1 << endl;

#ifdef _DEBUG
	_CrtDbgBreak();
#endif
	return EXIT_SUCCESS;
}



#include <queue>

// Classe utilisée par la liste de priorité des noeuds :
// Détermine si un noeud est (strictement) moins prioritaire qu'un autre
// en regardant si la longueur de son plus court chemin est supérieur.
template<class DjNodeInfo>
class DjNodeComparator
{
protected:
	const vector<DjNodeInfo>& dj;

public:
	DjNodeComparator(const vector<DjNodeInfo>& djInfos)
		: dj(djInfos) { }
	bool operator()(unsigned int node1, unsigned int node2)
	{
		return (dj[node1].totalCost > dj[node2].totalCost);
	}
};
// Algorithme de Dijkstra d'après le cours de RO :
template<class Graphe, class Noeud, class Lien>
void Dijkstra<Graphe, Noeud, Lien>::computeShortestPathsFrom(unsigned int startNode)
{
	// Réinitialise les informations sur les noeuds
	dj.clear();
	dj.resize(g.size());

	// Indique le coût du premier noeud et l'ajoute à la liste des noeuds à parcourir
	dj[startNode].totalCost = 0;
	DjNodeComparator<DjNodeInfo> cmp(dj);
	priority_queue<unsigned int, vector<unsigned int>, DjNodeComparator<DjNodeInfo> > nodesToSee(dj);
	nodesToSee.push(startNode);

	while (!nodesToSee.empty())
	{
		unsigned int node = nodesToSee.top();
		nodesToSee.pop();
		dj[node].alreadyVisited = true;
		unsigned int nodeTotalCost = dj[node].totalCost;

		const auto& links = g[node].getLinks();
		for (auto it = links.begin(); it != links.end(); ++it)
		{
			unsigned int targetNode = it->getTargetIndex();
			if (dj[targetNode].alreadyVisited)
				continue;

			unsigned int newCost = nodeTotalCost + it->getCost();
			if (newCost < dj[targetNode].totalCost)
			{
				dj[targetNode].totalCost = newCost;
				dj[targetNode].previousNode = node;
				nodesToSee.push(targetNode);
			}
		}
	}
}
template<class Graphe, class Noeud, class Lien>
bool Dijkstra<Graphe, Noeud, Lien>::canReachNode(unsigned int node) const
{
	return (dj[node].totalCost != (unsigned int)(-1));
}
template<class Graphe, class Noeud, class Lien>
unsigned int Dijkstra<Graphe, Noeud, Lien>::getCostTo(unsigned int node) const
{
	return dj[node].totalCost;
}
template<class Graphe, class Noeud, class Lien>
deque<unsigned int> Dijkstra<Graphe, Noeud, Lien>::getShortestPathTo(unsigned int endNode) const
{
	deque<unsigned int> l;
	while (endNode != (unsigned int)(-1))
	{
		l.push_front(endNode);
		endNode = dj[endNode].previousNode;
	}
	return l;
}
