#include<bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long int
using namespace std;

int arr[100005];
char pol1[10],pol2[10];
char abc[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
//map<char,int> mp;
//set <pair <int,char> > v;
vector <string> v;
int main()
{
           freopen("in.txt","r",stdin);
           freopen("out.txt","w",stdout);

         int t,l1,l2;
         string s1,s2;
    cin>>t;

    for(int tt=1;tt<=t;tt++)
    {
        int n;
        cin>>n;
        int sum=1;
        int mxi=-10000;
        for(int i=0;i<n;i++)
                cin>>arr[i];

        cout<<"Case #"<<tt<<": ";;

        while(sum>0)
        {
            sum=0;
            int mxi1=-1000;
            int mxi2=-1000;
            int ind1,ind2;
             string tmp="";
            for(int i=0;i<n;i++){
                sum+=arr[i];
                if(arr[i]>=mxi1) {
                        mxi1=arr[i];
                ind1=i;
            }
            }
            if(sum==0) break;
            for(int i=0;i<n;i++)
            {
                if(arr[i]>mxi2&&arr[i]<=mxi1&&i!=ind1)
                {
                    mxi2=arr[i];
                    ind2=i;
                }
            }
            arr[ind1]--;
            arr[ind2]--;

            int mx1=0;
            int tsum=0;
            for(int i=0;i<n;i++)
            {
                if(arr[i]>mx1)
                    mx1=arr[i];

                    tsum+=arr[i];
            }
            int r=(tsum/2)+1;
            if(mx1>=r)
            {
               tmp+=char(65+ind1);
               arr[ind2]++;
               v.push_back(tmp);
            }
            else
            {
                tmp+=char(65+ind1);
                tmp+=char(65+ind2);
                v.push_back(tmp);
            }
        }
            for(int i=0;i<v.size();i++)
                cout<<v[i]<<" ";

             cout<<endl;
             v.clear();
        }

       return 0;
}
