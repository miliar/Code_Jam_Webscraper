#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

struct node {
    int x;
    int y;
};

int main()
{
    int t,c=1;
    cin >> t;
    while(t--){
        double f,d,v;
        node n1;
        int i,j,k,l=0,m=0,n,cnt1=0,cnt2=0,r=0,x1,x2;
        cin >> n;
        string s1,s2;
        vector<double>v1,v2,v3,v4,v5;
        int flag=0,flag1=0;
        int ar[1001]={0},br[1001]={0};
        for(i=0;i<n;i++){
            cin >> d;
            v1.push_back(d);
        }
        for(i=0;i<n;i++){
            cin >> d;
            v2.push_back(d);
        }
        v3=v1;
        v4=v2;
        sort(v4.begin(),v4.end());
        sort(v3.begin(),v3.end());
        for(i=0;i<v1.size();i++){
            for(j=0;j<v2.size();j++){
                if(v4[j]>v3[i] && ar[j]==0){
                    ar[j]=1;
                    break;
                }
            }
        }
        for(i=0;i<v1.size();i++){
            if(ar[i]==0)
                cnt2++;
        }
        cnt1=n;
        for(i=0;i<v1.size();i++){
                if(v3[i]<v4[0]){
                    br[v1.size()-r]=1;
                    r++;
                    m++;
                    x1=r+m;
                    flag=1;
                }
                if(flag==0){
                    for(j=0;j<v1.size();j++){
                        if(v3[i]>v4[j] && br[j]==0){
                            flag1=1;
                            br[j]=1;
                            break;
                        }
                    }
                    if(flag1==0){
                        m++;
                        br[v1.size()-r]=1;
                        r++;
                        x2=m+r;
                    }
                    flag1=0;
                }
                flag=0;
                flag1=0;
            }
        cnt1=cnt1-m;
        n1.x=cnt1;
        n1.y=cnt2;
        cout << "Case " << "#" << c << ": " << n1.x << " " << n1.y << endl;
        c++;
    }
    return 0;
}
