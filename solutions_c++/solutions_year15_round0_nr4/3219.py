/*using namespace std;
#include<bits/stdc++.h>
int main(){    
	int t,n,l,r,m,x,y;
	cin>>t;
	while(t--){
		cin>>n>>x>>y>>m;
		vector<pair<int,int> >v;
		for(int i=0;i<m;i++){
			x=(x+7)%(n-1);
			y=(y+11)%n;
			//if(x>y)swap(x,y);
			if(x>y)v.push_back(make_pair(y,x));
			else v.push_back(make_pair(x,y));
		}
		sort(v.begin(),v.end());
		for(int i=0;i<v.size();i++)
		cout<<v[i].first<<" "<<v[i].second<<endl;
	}
	
}*/
#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
		ifstream in("D1.in");
        ofstream out("file3.txt");
        int t,p=0;
        in>>t;
        while(t--)
        {
               int x,r,c;
               in>>x>>r>>c;
               int f=0;
               if(x==1)f=1;
               else if(x==2){
               	if ((r*c)%2==0){
               		f=1;
               	}
               }
               else if(x==3){
               	if((r*c)==6||(r*c)==9||(r*c)==12){
               		f=1;
               	}
               }
               else if(x==4){
               	if((r*c)==12||(r*c)==16){
               		f=1;
               	}
               }
               if (f)out<<"Case #"<< p+1 <<": "<<"GABRIEL" << endl;
               else out<<"Case #"<< p+1 <<": "<<"RICHARD" << endl;
               p++;
        }
        return 0;
}
