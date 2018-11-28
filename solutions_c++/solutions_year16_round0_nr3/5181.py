#include <iostream>
#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

class DisjointSets
{
public:

	// Create an empty DisjointSets data structure
	DisjointSets();
	// Create a DisjointSets data structure with a specified number of elements (with element id's from 0 to count-1)
	DisjointSets(int count);
    // Copy constructor
    DisjointSets(const DisjointSets & s);
	// Destructor
	~DisjointSets();
	int FindSet(int element) const;
	void Union(int setId1, int setId2);
	// Add a specified number of elements to the DisjointSets data structure. The element id's of the new elements are numbered
	// consequitively starting with the first never-before-used elementId.
	void AddElements(int numToAdd);
	int NumElements() const;
	int NumSets() const;

private:
	struct Node
	{
		int rank;
		int index;
		Node* parent;
	};

	int m_numElements; // the number of elements currently in the DisjointSets data structure
	int m_numSets; // the number of sets currently in the DisjointSets data structure.
	std::vector<Node*> m_nodes;
};

DisjointSets::DisjointSets()
{
	m_numElements = 0;
	m_numSets = 0;
}

DisjointSets::DisjointSets(int count)
{
	m_numElements = 0;
	m_numSets = 0;
	AddElements(count);
}

DisjointSets::DisjointSets(const DisjointSets & s)
{
	this->m_numElements = s.m_numElements;
	this->m_numSets = s.m_numSets;
	m_nodes.resize(m_numElements);
	for(int i = 0; i < m_numElements; ++i)
		m_nodes[i] = new Node(*s.m_nodes[i]);
	for(int i = 0; i < m_numElements; ++i)
		if(m_nodes[i]->parent != NULL)
			m_nodes[i]->parent = m_nodes[s.m_nodes[i]->parent->index];
}

DisjointSets::~DisjointSets()
{
	for(int i = 0; i < m_numElements; ++i)
		delete m_nodes[i];
	m_nodes.clear();
	m_numElements = 0;
	m_numSets = 0;
}

int DisjointSets::FindSet(int elementId) const
{
	assert(elementId < m_numElements);

	Node* curNode;
	curNode = m_nodes[elementId];
	while(curNode->parent != NULL)
		curNode = curNode->parent;
	Node* root = curNode;
	curNode = m_nodes[elementId];
	while(curNode != root)
	{
		Node* next = curNode->parent;
		curNode->parent = root;
		curNode = next;
	}

	return root->index;
}

void DisjointSets::Union(int setId1, int setId2)
{
	assert(setId1 < m_numElements);
	assert(setId2 < m_numElements);

	if(setId1 == setId2)
		return; // already unioned

	Node* set1 = m_nodes[setId1];
	Node* set2 = m_nodes[setId2];

	// Determine which node representing a set has a higher rank. The node with the higher rank is
	// likely to have a bigger subtree so in order to better balance the tree representing the
	// union, the node with the higher rank is made the parent of the one with the lower rank and
	// not the other way around.
	if(set1->rank > set2->rank)
		set2->parent = set1;
	else if(set1->rank < set2->rank)
		set1->parent = set2;
	else // set1->rank == set2->rank
	{
		set2->parent = set1;
		++set1->rank; // update rank
	}

	// Since two sets have fused into one, there is now one less set so update the set count.
	--m_numSets;
}

void DisjointSets::AddElements(int numToAdd)
{
	assert(numToAdd >= 0);

	// insert and initialize the specified number of element nodes to the end of the `m_nodes` array
	m_nodes.insert(m_nodes.end(), numToAdd, (Node*)NULL);
	for(int i = m_numElements; i < m_numElements + numToAdd; ++i)
	{
		m_nodes[i] = new Node();
		m_nodes[i]->parent = NULL;
		m_nodes[i]->index = i;
		m_nodes[i]->rank = 0;
	}

	// update element and set counts
	m_numElements += numToAdd;
	m_numSets += numToAdd;
}

int DisjointSets::NumElements() const
{
	return m_numElements;
}

int DisjointSets::NumSets() const
{
	return m_numSets;
}
#include <iostream>

using namespace std;
struct coo{
	int node;
	int end;
	int val;
};
typedef struct coo element;
inline bool comp(element a, element b)
{
	return a.val<b.val;
}

void printElementSets(const DisjointSets & s)
{
	for (int i = 0; i < s.NumElements(); ++i)
		cout << s.FindSet(i) << "  ";
	cout << endl;
}

int main()
{
	int t;
	cin>>t;
	while(t--){
		int n,m,k;
		scanf("%d%d%d",&n,&m,&k);
		DisjointSets d(n);
		vector<element> v(m);
		for(int i=0;i<m;i++){
			element temp;
			scanf("%d%d%d", &temp.node,&temp.end,&temp.val);
			temp.node--;
			temp.end--;
			v[i] = temp;
		}
		sort(v.begin(), v.end(), comp);
		long long ans = 0;
		int flag = 0;
		if(k>=n)
			flag = 1;
		else{
		for(int i=0;i<m;i++){
			if(d.NumSets()<=k){
				flag =1;
				break;
			}
			element temp = v[i];
			if(d.FindSet(temp.node) != d.FindSet(temp.end)){
				d.Union(d.FindSet(temp.node),d.FindSet(temp.end));
				ans += temp.val;
			}
			if(d.NumSets() <=k){
				flag = 1;
				break;
			}
		}
		}
		if(flag == 0){
			cout<<"Impossible!"<<endl;
			continue;
		}
		cout<<ans<<endl;
	}
	return 0;
}
