#include<bits/stdtr1c++.h>
using namespace std;



int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
      freopen("2.txt","w",stdout);
        
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t,ic=1;
    cin>>t;
    while(t--)
    {
        vector<double> arr,v;
        set<double> st;
        int n;
        cin>>n;
        arr.resize(n);
        v.resize(n);
        
        for(int i=0;i<n;i++)
            cin>>arr[i];
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
            st.insert(v[i]);
        }
        
        sort(arr.begin(),arr.end());
        sort(v.begin(),v.end());
        
            int dw=0,w=0;
        int s1,e1,s2,e2;
        s1=s2=0;
        e1=e2=n-1;
        while(e1>=s1 && e2>=s2)
        {
            if(arr[s1]> v[s2])
            {
                dw++;
                s1++;
                s2++;
            }
            else 
            {
                //dw--;
                s1++;
                e2--;
            }
            /*else if(arr[e1]>v[e2])
            {
                e1--;
                s2++;
            }
            else
            {
                dw--;
                e2--;
                s1++;
            }*/
        }
  
      
        /*for(int i=0;i<n;i++)
            cout<<arr[i]<<" ";
        cout<<endl;
        for(int i=0;i<n;i++)
            cout<<v[i]<<" ";
        cout<<endl;*/

        for(int i=0;i<n;i++)
        {
            if(lower_bound(st.begin(),st.end(),arr[i])== st.end())
            {
                w++;
                st.erase(st.begin());
            }
            else
                st.erase(lower_bound(st.begin(),st.end(),arr[i]));
        }
     cout<<"Case #"<<ic++<<": ";
     cout<<dw<<" "<<w<<endl;   
    }
    return 0;
    
}
