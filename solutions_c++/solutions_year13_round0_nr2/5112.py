#include <iostream>
//#include <map>  
//#include <vector>
#include <set>  
#include <string>
#include <string.h>
#include <fstream>
//#include <algorithm>  

using namespace std;

int n,m,count1;
char fn[26]="count/documents/1.txt";

//map<string,int> fnc;
//vector<string> fstr;
//set<string> stop;
//vector<pair<string,int> > tVector;  
int map[100][100];

/*int index(string s){
	int i;
	for(i=0;i<40;i++){
		if(s.compare(feature[i])==0)return i;
	}
	return -1;
}*/

/*int cmp(const pair<std::string, int>& x, const pair<std::string, int>& y){  
	return x.second > y.second;  
}  
   
void sortMapByValue(map<std::string, int>& tMap, vector<std::pair<std::string, int> >& tVector){  
	for(map<string, int>::iterator curr = tMap.begin(); curr != tMap.end(); curr++){  
		tVector.push_back(make_pair(curr->first, curr->second));  
	}  
   
	sort(tVector.begin(), tVector.end(), cmp);  
}  

vector<string> split(const string& src, string separate_character)
{
    vector<string> strs;
    int separate_characterLen = separate_character.size();//分割字符串长度，这样就可以支持多字 符串的分隔符
    int lastPosition = 0, index = -1;
    while (-1 != (index = src.find(separate_character, lastPosition)))
    {
        strs.push_back(src.substr(lastPosition, index - lastPosition));
        lastPosition = index + separate_characterLen;
    }
    string lastString = src.substr(lastPosition);
    if (!lastString.empty())
    strs.push_back(lastString);
    return strs;
}



void printSet(set<string> s)
{
	copy(s.begin(), s.end(), ostream_iterator<string>(cout, ", ") );
	cout<<endl;
}


*/

int judge(int x,int y){
	int i,j;
	//int fx=1,fy=1;
	for(i=0;i<m;i++){
		if(map[x][i]>map[x][y])break;
	}
	if(i==m)return 1;
	for(j=0;j<n;j++){
		if(map[j][y]>map[x][y])break;
	}
	if(j==n)return 1;
	return 0;
}


void main() {
    int t=0,i1=0,flag,j;
	//int c=0;
	string word1,word2,filename;
	string lines;
	count1=0;
	ifstream in("D:\\Program Files\\Microsoft Visual Studio\\MyProjects\\poj\\B-large.in");
	ofstream examplefile ("test.txt");//count/test.txt
	if(in && examplefile.is_open()){
		//getline (in, lines);
		in>>count1;
		cout<<count1<<endl;
		//getline (in, lines);
		for(int i4=0;i4<count1;i4++){
			
			examplefile<<"Case #"<<++t<<": ";
					
			in>>n>>m;
			cout<<"n:"<<n<<" m:"<<m<<endl;
			for(i1=0;i1<n;i1++){
				for(j=0;j<m;j++){
					in>>map[i1][j];
				}				
			}
			flag=1;
			for(i1=0;i1<n;i1++){
				for(j=0;j<m;j++){
					if(judge(i1,j)==0){
						flag=0;		
						break;
					}
					//cout<<map[i1][j]<<" ";
				}//cout<<endl;				
			}
			
			if(flag){
				cout<<"YES"<<endl;
				examplefile<<"YES"<<endl;
			}else{
				cout<<"NO"<<endl;
				examplefile<<"NO"<<endl;
			}
			//cout<<"c:"<<c<<endl;
		//	cout<<endl;
		}
	/*	while(getline (in, lines)){  // have no '\n',
			
		
//			cout<<lines<<" "<<lines.size()<<endl;
//			examplefile<<"Case #"<<t++<<": ";
//			for(int i4=0;i4<lines.size();i4++){
//				
//			}
			examplefile<<endl;
	
			//break;
			 // ;
			// store the lines to a vector or list, use method insert
		}*/
		// ...
	}else{
		// open file fail....
	} 
	in.close();
	examplefile.close();

	/*ofstream examplefile ("count/本.txt");
	if(examplefile.is_open()) {
		examplefile << "This is a line.\n";
		examplefile << "This is another line.\n";
		examplefile.close();
	}*/
	
   // return 0;
}
