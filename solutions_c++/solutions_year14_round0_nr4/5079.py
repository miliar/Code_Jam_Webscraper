#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
    int t,c=1;
    cin >> t;
    while(t--){
        double f,d,v;
        int i,j,k,l=0,m=0,n,c1=0,c2=0,r=0,flag=0,flag1=0;
        cin >> n;
        vector<double>v1,v2,v3,v4,v5;
        int ar[11]={0},br[11]={0};
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
        v5=v2;
        sort(v5.rbegin(),v5.rend());
        sort(v4.begin(),v4.end());
        sort(v3.begin(),v3.end());
        for(i=0;i<v1.size();i++){
            for(j=0;j<v2.size();j++){
                if(v4[j]>v3[i] && ar[j]==0){
                    //cout << v4[j] << " " << v3[i] << endl;
                    ar[j]=1;
                    break;
                }
            }
        }
        for(i=0;i<v1.size();i++){
            if(ar[i]==0)
                c2++;
        }
        c1=n;
        for(i=0;i<v1.size();i++){
                if(v3[i]<v4[0]){
                    br[v1.size()-r]=1;
                    r++;
                    m++;
                    flag=1;
                }
                if(flag==0){
                    for(j=0;j<v1.size();j++){
                        if(v3[i] > v4[j] && br[j]==0){
                            flag1=1;
                            br[j]=1;
                            break;
                        }
                    }
                    if(flag1==0){
                        m++;
                        br[v1.size()-r]=1;
                        r++;
                    }
                }
                flag=0;
                flag1=0;
            }
            c1=c1-m;
        cout << "Case " << "#" << c << ": " << c1 << " " << c2 << endl;
        c++;
    }
    return 0;
}
