#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>

using namespace std;

int n;
int times;
int f[1100];
vector<double> p,q;
double x,y,z;
const double eps=1e-7;

int main(){
	freopen("D-large.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>times;
	for (int ti=1;ti<=times;ti++){
		cin >> n;
		p.clear();
		q.clear();
		for (int i=0;i<n;i++){
            cin>>x;
            p.push_back(x);
        }
		for (int i=0;i<n;i++){
            cin>>x;
            q.push_back(x);
        }        
        sort(p.begin(),p.end());
        sort(q.begin(),q.end());
        memset(f,0,sizeof(f));
        int ans1,ans2;
        ans1=ans2=0;
        for (int i=0;i<n;i++){
            int bo=1;
            for (int j=0;j<n;j++)
                if (f[j]==0 && q[j]-p[i]>eps){
                   bo=0;
                   ans2++;
                   f[j]=1;
                   break;
                }
            if (bo)
               for (int j=0;j<n;j++)
                if (f[j]==0 && q[j]-p[i]<eps){
                   f[j]=1;
                   break;
                }
        }
        memset(f,0,sizeof(f));
        for (int i=0;i<n;i++){
            int bo=1;
            for (int j=0;j<n;j++)
                if (f[j]==0 && p[j]-q[i]>eps){
                   bo=0;
                   ans1++;
                   f[j]=1;
                   break;
                }
            if (bo)
               for (int j=0;j<n;j++)
                if (f[j]==0 && p[j]-q[i]<eps){
                   f[j]=1;
                   break;
                }
        }
		//cout<<"Case #"<<ti<<": ";
		printf("Case #%d: %d %d\n",ti,ans1,n-ans2);
	}
	return 0;
}
