#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[6007];
    long int te,step=0,l=0;
    long int n,i,j,maximum=0,min1,sum,r=1,s=2;
    float t;
    r=s;
    s=r;
    ifstream fin;
    ofstream fout;
    fin.open("sum22.in",ios::in);
    fout.open("a.txt",ios::out);
    fin>>te;
    while(te--)
    {
        maximum=0;
        fin>>n;
        for(i=0 ; i<n ; i++)            //Finds out the maximum
        {
            s=r;                     //lalalalallalalalalalla
            fin>>a[i];                  //jingalalahooo
            if(a[i]>maximum)
                maximum=a[i];
        }

        min1 = maximum ;
        for(i=1; i<=maximum ;i++)
        {
            sum = i ;
            for(j=0 ; j<n ; j++)            //WOOOOOHOOO
            {
                r=s;
                if(a[j] > i)
                {
                    if(a[j]%i == 0)
                        sum += (a[j]/i-1);             //WOOOHOOOOO
                    else
                        sum += (a[j]/i);
                }
            }
            min1 = min(min1,sum);
        }
        ++step;
        fout<<"Case #"<<step<<": "<<min1<<endl;
    }
    return 0;
}
