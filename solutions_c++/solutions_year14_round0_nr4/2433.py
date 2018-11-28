#include<iostream>
#include<algorithm>
//#include<vector>

using namespace std;
main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        int N,j,k;
        cin>>N;
        double a[1010],b[1010];
        double x;
        for(j=0;j<N;j++)
        {
            cin>>a[j];
            //s1.insert(x);
        }
        for(j=0;j<N;j++)
        {
            cin>>b[j];
            //s2.insert(x);
        }
        sort(a,a+N);
        sort(b,b+N);
        //set<double>::iterator it1=s1.begin();
        //set<double>::iterator it2=s2.begin();
        j=0;k=0;int c=0;
        while(j!=N)
        {
            if(k==N)
            {c++;j++;}
            else if(a[j]<b[k])
            {
                j++;k++;
            }
            else if(a[j]>b[k])
            {
                while(a[j]>b[k]&&k!=N)
                    k++;
            }
        }
        j=0;k=0;int d=0;
        while(j!=N)
        {
            if(a[j]<b[k]){
            while(a[j]<b[k]&&j!=N)
                {j++;}}
            else if(a[j]>b[k])
            {
                d++;j++;k++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<d<<" "<<c<<endl;
        //v.clear();
        //s1.clear();
        //s2.clear();
    }
}
