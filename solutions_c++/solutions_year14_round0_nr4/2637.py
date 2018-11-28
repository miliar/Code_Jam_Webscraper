#include<fstream>
using namespace std;
int main()
{
    int t,i,j,m,n,k,l,s,c=1;
    float a[1000],b[1000],temp;
    ifstream fin;
    ofstream fout;
    fin.open("abc.in");
    fout.open("out.out");
    fin>>t;
    while(t--)
    {
        fin>>n;
        for(i=0;i<n;i++)
            fin>>a[i];
        for(i=0;i<n;i++)
            fin>>b[i];
        for(i=0;i<n;i++)
        {
            for(j=i;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;
                }
                if(b[i]>b[j])
                {
                    temp=b[i];
                    b[i]=b[j];
                    b[j]=temp;
                }
            }
        }
        k=l=n-1;
        m=0;
        i=0;
        j=0;
        while(a[k]<b[l])
        {
            l--;
            i++;
        }
        for(;i<n;i++)
        {
            if(a[i]>b[j])
            {
                    m++;
                    j++;
            }
        }
        for(i=n-1,j=0,k=n-1,s=0;i>=0;i--)
        {
            if(a[i]>b[k])
            {
                s++;
                j++;
            }
            else
                k--;
        }
        fout<<"Case #"<<c<<": "<<m<<" "<<s<<endl;
        c++;
    }
    fin.close();
    fout.close();
    return 0;
}
        
                    
        
        
