#include<iostream>
#include<fstream>

using namespace std;

int j;
int arr[10];

void ini()
{
    for(j=0;j<10;j++) arr[j]=0;
}

void mark(int q)
{
    arr[q]=1;
    //cout<<"\nMarking number:"<<q;
}

int check()
{
    int w=0, prod=1;
    while(w<10)
    {
        prod = prod * arr[w];
        //cout<<"\n product: "<<prod;
        w++;
    }

    if(prod==1)
    {
        return 1;
    }

    else
        return 0;
}

int compute(int x)
{
    int b=1;
    ini();

    while(b<100)
    {
        int y=b*x;
       // cout<<"\n y="<<y;

        while(y)
        {
            mark(y%10);
            y=y/10;
        }

        if(check())
        {
            return b*x;

        }
        b++;

    }



    if(b==100)return -1;
}





int main()
{
    ifstream fin;
    fin.open("A-large.in",ios::in);

    int i, t;
    fin>>t;
    int a[t];
    for( i=0;i<t;i++)
    {
        fin>>a[i];
        a[i]=compute(a[i]);
    }

    ofstream fout;
    fout.open("output.txt",ios::out);


    for(i=0;i<t;i++)
    {

        if(a[i]!= -1){fout<<"\nCase #"<<i+1<<": "<<a[i];}
        else fout<<"\nCase #"<<i+1<<": INSOMNIA";
    }

fout.close();
return 0;
}
