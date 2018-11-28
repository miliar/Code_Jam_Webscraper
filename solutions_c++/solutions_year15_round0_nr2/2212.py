#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<fstream>
using namespace std;

int SZ,arr1[1003];
int FS,arr2[1003];
bool f(int spe,int mid)
{
    FS=0;
    for(int i=1; i<=SZ; i++)
    {
        if(arr1[i]<=mid)
        {
            //Do nothing! :D
        }
        else if(arr1[i]>mid)
        {
            int difference=arr1[i]-mid;
            FS++;
            arr2[FS]=difference;
        }
    }
    int id=1;
    while( id<=FS )
    {
        if(arr2[id]>0 && spe==0)
        {
            return false;
        }
        if(mid>=arr2[id])
        {
            id++;
            spe--;
        }
        else
        {
            arr2[id]-=mid;
            spe--;
        }
    }
    return true;
}
int main()
{
    ifstream input;
    ofstream output;
    input.open("B-large.in");
    output.open("out.txt");
    int tc,D,P,c;
    input>>tc;
    c=0;
    for(int testcase=1;testcase<=tc;testcase++)
    {
        c++;
        SZ=0;
        input>>D;
        for(int i=1; i<=D; i++)
        {
            input>>P;
            SZ++;
            arr1[SZ]=P;
        }
        int ans=1000006;
        bool fnd;
        for(int special=0; special<=1000; special++)
        {
            int low=1;
            int up=1000;
            int mid;
            while(low<up)
            {
                mid=low+(up-low)/2;
                fnd=f(special,mid);
                if(fnd==false)
                {
                    low=mid+1;
                }
                else
                {
                    up=mid;
                }
            }
            if(special+low<ans)
            {
                ans=special+low;
            }
        }
        output<<"Case #"<<testcase<<": "<<ans<<endl;
    }
    return 0;
}
