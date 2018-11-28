#include<bits/stdc++.h>

using namespace std;

#define p pair<int,int>
#define f first
#define s second


int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    int i,j;
    int k=0;

    scanf("%d",&t);

    while(t--)
    {
        k++;
        int n;
        scanf("%d",&n);

        int hash[26]={0};
        int sum=0;
        int fu=0;
        vector<p> v;
        vector<string> ans;

        for(i=0;i<n;i++)
        {
            p p1;
            int x;
            cin>>x;
            sum+=x;
            p1.f=x;
            p1.s=i;

            v.push_back(p1);
        }

        sort(v.begin(),v.end());
        //cout<<"adi\n"<<sum<<endl;
        while(1)
        {
            if(sum<=0)
                break;
            string s;

            if(v[v.size()-1].f==1 && n%2!=0)
            {
                fu=1;
                s+=(v[v.size()-1].s + 'A');
                v[v.size()-1].f--;
                //cout<<"reduce\n"<<v[v.size()-1].f<<" "<<sum<<endl;
                sum--;
                ans.push_back(s);
                s.clear();
            }

            sort(v.begin(),v.end());
            if(sum<=0)
                break;

            s+=(v[v.size()-1].s + 'A');
            v[v.size()-1].f--;
            if(v[v.size()-1].f==0)
                n--;
            sum--;
            //cout<<"sum=="<<sum<<endl;
            if(sum<=0)
            {
                ans.push_back(s);
                break;
            }

            sort(v.begin(),v.end());
            s+=(v[v.size()-1].s + 'A');
            v[v.size()-1].f--;
            if(v[v.size()-1].f==0)
                n--;
            ans.push_back(s);
            sort(v.begin(),v.end());
            sum--;
        }

        printf("Case #%d: ",k);
        //cout<<"adi\n";
        for(i=0;i<ans.size();i++)
            cout<<ans[i]<<" ";
        cout<<endl;
    }

    return 0;
}
