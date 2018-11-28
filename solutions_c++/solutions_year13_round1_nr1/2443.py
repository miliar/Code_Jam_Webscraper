/*#include<iostream>
#include<fstream>

using namespace std ;
int main(){

	ifstream fin("s.in");
	ofstream fout("s.out");
	long long n ,t , r , count=0; 
	fin>>n ; 
	//cout<< n << endl; 
	for(int i = 1 ; i <=n ; i++){
		fin >> r >> t ;
		//cout<< n << endl; 
		int O1 = r*r ; 
		int O2 = (r+1)*(r+1) ; 
		int OO = O2-O1 ; 
		for(int q = t ; q>0 ;){
			//cout<< n << endl; 
			q=q-OO;
			if(q<=0) break ; 
			r++;
			O1 = r*r ; 
			O2 = (r+1)*(r+1) ; 
			OO = O2-O1 ;
			count++ ;
		}
		fout<< "Case #"<<i<<": "<< count << endl;
	}
	return 0 ; 
}

#include<iostream> 
using namespace std; 

int main()
{
 freopen("s.in","r",stdin);
 freopen("s.out","w",stdout);
 int i=1,te,count;
 cin>>te;
 long long int R,T,size;
 for(;i<=te;i++){
  count = 0;
  cin>>R>>T;
  size = (R+1)*(R+1) - R*R;
  while(size <= T){
   //cout<<size<<"\n";
   count++;
   T-=size;
   size = size+4;
  }
  printf("Case #%d: %d\n",i,count);
 }

 return 0;
}*/

#include<iostream>
#include<fstream>

using namespace std ;
int main(){

	ifstream fin("s.in");
	ofstream fout("s.out");
	long long n ,t , r , count=0;
	fin >> n ; 
	for(int i = 1 ; i<=n ; i++){
		fin >> r >> t ;
		long long s = ((r+1)*(r+1))-((r)*(r));
		for(int q = 1 ; ;q++){
			if(t-s>=s+4){
				t-=s ; 
				s+=4 ; 
			}
			else{
				count = q ;
				break;
			}
		}
		fout<< "Case #"<<i<<": "<< count << endl;
	}

}