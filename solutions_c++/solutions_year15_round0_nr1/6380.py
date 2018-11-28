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
#
using namespace std;
int main()
{
		ifstream in("A-large.in");
        ofstream out("file.out");
        int t,p=0;
        in>>t;
        while(t--)
        {
                int m;
                in>>m;
                string ss;
                in>>ss;
                int k=ss.size(),ans=0,s=0;
                int cum[k];
				s=ss[0]-'0';
                if(s==0)ans++;
                s+=ans;
                cum[0]=s;
                for(int i=1;i<k;i++){
                	if(cum[i-1]<i){
                		ans+=i-cum[i-1];
                		//cout<<ans<<endl;
                		s+=i-cum[i-1];
                	}
                	s+=ss[i]-'0';
                	cum[i]=s;
	            }
				out<<"Case #"<< p+1 <<": "<< ans << endl;
                p++;
        }
        return 0;
}
