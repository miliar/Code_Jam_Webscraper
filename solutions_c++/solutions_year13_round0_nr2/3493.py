#include<iostream>
#include<vector>
#include<algorithm>
using std::sort;
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::string;
typedef struct Node{
	int x;
	int y;
	int height;
}Node;
bool cmp(Node n1, Node n2){
	if(n1.height > n2.height)return true;
	return false;
}
bool checkLine(vector<vector<int>>& board, int x, int y){
	bool flag = true;
	bool result = false;
	for(int i=0; i<board[x].size(); i++){
		if(board[x][i] != 0 && board[x][i] != board[x][y]){
			flag = false;
			break;
		}
	}
	if(flag){
		for(int i=0; i<board[x].size(); i++){
			board[x][i] = 0;
		}
		result = true;
	}
	flag = true;
	for(int i=0; i<board.size(); i++){
		if(board[i][y] != 0 && board[i][y] != board[x][y]){
			flag = false;
			break;
		}
	}
	if(flag){
		for(int i=0; i<board.size(); i++){
			board[i][y] = 0;
		}
		result = true;
	}
	return result;
}
void check(vector<vector<int>> board){
	vector<Node> queue;
	for(int i=0; i<board.size(); i++){
		for(int j=0; j<board[i].size(); j++){
			Node node;
			node.x = i;
			node.y = j;
			node.height = board[i][j];
			queue.push_back(node);
		}
	}
	sort(queue.begin(), queue.end(), cmp);
	while(!queue.empty()){
		Node n = queue.back();
		queue.pop_back();
		if(board[n.x][n.y] == 0)continue;
		bool result = checkLine(board, n.x, n.y);
		if(!result){
			cout<<"NO"<<endl;
			return;
		}
	}
	cout<<"YES"<<endl;
}
int main(){
	int caseNo;
	cin>>caseNo;
	int n, m;
	for(int count = 0; count<caseNo; count++){
		cout<<"Case #"<<count+1<<": ";
		cin>>n>>m;
		vector<vector<int>> board;
		for(int i=0; i<n; i++){
			vector<int> line;
			for(int j=0; j<m; j++){
				int height;
				cin>>height;
				line.push_back(height);
			}
			board.push_back(line);
		}
		check(board);

	}
	
	return 0;
}