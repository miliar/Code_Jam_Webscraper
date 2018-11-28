#include<iostream>
#include<fstream>
#include<conio.h>
#include<set>
#include<windows.h>
using namespace std;
#define gc getchar
int read_int() {
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  int ret = 0;
  while(c>='0' && c<='9') {
    ret = 10 * ret + c - 48;
    c = gc();
  }
  return ret;
}
int main(){
	ifstream ifile("A-small-attempt1.in");
	if(!ifile)cout<<"can't open!"<<endl;
	int t, i, j, temp, n=1, r1,r2,ans=0,num;
	set<int> r1Elem[4],r2Elem[4];
	set<int>::iterator itr;
	//t=read_int();
	ifile>>t;
	ofstream ofile("A-small-attempt0.out");
	while(t--){
		ans=0;
		//r1=read_int();
		ifile>>r1;
		r1--;
		for( i=0;i<4;i++){
				for(j=0;j<4;j++){
				  ifile>>temp;
				  if((i==r1))r1Elem[i].insert(temp);
				  //if((i==r1))cout<<temp<<" ";
				}
				//cout<<endl;
		}
		ifile>>r2;
		r2--;
		for( i=0;i<4;i++){
			    for(j=0;j<4;j++){
					ifile>>temp;
					if(i==r2)r2Elem[i].insert(temp);
					//if(i==r2)cout<<temp<<" ";
				}	
			//cout<<endl;
		}
		itr=r1Elem[r1].begin();
		while(itr!=r1Elem[r1].end()&&ans<3){
			//cout<<r2Elem[r2].count(*itr)<<" for elem"<<*itr<<endl;
			if(r2Elem[r2].count(*itr)>0){
				num=*itr;
				ans++;	
			}
			itr++;
		}
		switch(ans){
			case 0:
				  ofile<<"Case #"<<n<<": Volunteer cheated!\n";
				break;
			case 1:
				  ofile<<"Case #"<<n<<": "<<num<<"\n";
				break;
			default:
				  ofile<<"Case #"<<n<<": Bad magician!\n";
				break;
		}
		n++;
		//system("pause");
		r1Elem[r1].erase(r1Elem[r1].begin(),r1Elem[r1].end());
		r2Elem[r2].erase(r2Elem[r2].begin(),r2Elem[r2].end());
		//cout<<r2Elem[r2].size()<<endl;
		//cout<<r1Elem[r1].size()<<endl;
	}	
}
