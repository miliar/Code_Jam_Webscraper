#include <iostream>
#include <vector>
#include <map>
#include <deque>
#define maxNode 100
using namespace std;

class graphApi{
  public:
  	int vertices;
  	int edges;
  	vector< pair<int,int> > adjacencyList[maxNode+1];
  	graphApi(int n,int m){
  		vertices = n;
  		edges = m;	
  	}
  	void printNum(){
  		cout << "Number of vertices " << vertices << "  " << "Number of edges " << edges << endl;
  	}
  	void addEdge(int start,int last,int weight){
  		if(!checkEdgeExist(start,last)){
  	    	if(start==last){
  	    		adjacencyList[start].push_back(make_pair(last,weight));
  	    	}
  	    	else{
  				adjacencyList[start].push_back(make_pair(last,weight));
  				adjacencyList[last].push_back(make_pair(start,weight));
  			}
  		}
  		else{
  			cout << "edge exist between these two nodes" << endl;
  		}
  	}

  	bool testInsertionofNode(int start,int end){
  		if(start > 0 && start <= vertices && end > 0 && end <= vertices){
  			return true;
  		}
  		else return false;
  	}

  	bool checkEdgeExist(int start,int end){
  		vector< pair<int,int> >::iterator it;
  		for(it = adjacencyList[start].begin();it!=adjacencyList[start].end();it++){
  			if(it->first == end){
  				return true;
  			}
  		}
  		return false;
  	}

  	void printAdjList(){
  		vector< pair<int,int> > :: iterator it;
  		for(int i=1;i<=vertices;i++){
  			cout << "node number " << i << "  ";
  			for(it=adjacencyList[i].begin();it!=adjacencyList[i].end();it++){
  				cout << it->first << "  " << it->second << " 	";
  			}
  			cout << endl;
  		}
  	}

  	void _dfs(int start,bool visited[]){
  		visited[start] = true;
  		cout << start << "	";
  		vector< pair<int,int> >::iterator it;
  		for(it= adjacencyList[start].begin();it!=adjacencyList[start].end();it++){
  			if(!visited[(it->first)]){
  				_dfs(it->first,visited);
  			}
  		}
  	}

  	void dfs(){
  		cout << "dfs called " << endl;
  		int start = 1;
  		dfs(start);
  	}

  	void dfs(int start){
  		bool *visited = new bool[vertices];
  		for(int i=0;i<vertices;i++){
  			visited[i] = false;
  		}
  		_dfs(start,visited);
  	}

  	void bfs(int start){
  		bool *visited = new bool[vertices];
  		for(int i=0;i<vertices;i++){
  			visited[i] = false;
  		}
  		deque<int> queue;
  		queue.push_back(start);

  		visited[start] = true;

  		while(!queue.empty()){
  			start = queue.front();
  			cout << start << "	";
  			queue.pop_front();
  			vector< pair<int,int> >::iterator it;
  			for(it=adjacencyList[start].begin();it!=adjacencyList[start].end();it++){
  				if(!visited[(it->first)]){
  					visited[(it->first)] = true;
  					queue.push_back(it->first);
  				}
  			}
  		}
  	}

  	void bfs(){
  		cout << "bfs called " << endl;
  		int start = 2;
  		bfs(start);
  	}

  	void 

};

int main(){
	int n,m;
	cin >> n >> m;
	graphApi g(n,m);
	g.printNum();
	for(int i=0;i<m;i++){
		int start,end,weight;
		cin >> start >> end >> weight;
		g.addEdge(start,end,weight);
	}
	g.printAdjList();
	g.dfs();
	g.bfs();
	return 0;
}