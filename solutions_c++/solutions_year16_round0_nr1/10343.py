#include<fstream>
#include<iostream>>
using namespace std;

int check(int a[])
{   int f=1;
    for(int i=0;i<10;i++)
        { if(a[i]==0)
            {   f=0;
                break;
            }
        }
    if(f==0)
    return 1;
    else return 0;
}


int main()
{
    int t,t1,n,i,last,d;
    ifstream txt;
    txt.open("txt.txt");
    txt>>t;
    t1=t;
    ofstream myfile;
    myfile.open("example.txt");
    while(t--)
    {
        txt>>n;
	if(n==0)
	{myfile<<"Case #"<<t1-t<<": INSOMNIA\n";
        cout<<"Case #"<<t1-t<<": INSOMNIA\n";
	continue;}
        myfile<<"Case #"<<t1-t<<": ";
        cout<<"Case #"<<t1-t<<": ";
        int a[10]={0};
        last=n;
        i=0;
    while(check(a))
        {   i++;
            n=last*i;
            while(n>0)
                {d=n%10;
                if(a[d]==0)
                a[d]=1;
                n=n/10;
                }
        }
        cout<<last*i<<endl;
      myfile<<last*i<<endl;
    }
    myfile.close();
    txt.close();
}
