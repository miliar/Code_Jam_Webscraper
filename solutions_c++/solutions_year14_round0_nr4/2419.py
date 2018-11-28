#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


int war(vector<double> a,vector<double> b)
{
    int res=0;
    int size=a.size();

    for(int i=0;i<size;i++)
    {
        for(int j=0;j<size;j++)
        {
            if(a[i]<b[j])
            {
                b[j]=-1;
                break;
            }
        }
    }

    for(int i=0;i<size;i++)
        if(b[i]==-1)res++;
    return size-res;

}
int dec_war(vector<double> a,vector<double> b)
{
    int size=a.size();
    int res=0;
    int i=0,j=0,k=size-1;

    while(i!=size)
    {
        if(a[i]>b[j])
        {
            i++;
            j++;
            res++;

        }
        else
        {
            i++;
            k--;
        }
    }
    return res;
}
int main()
{
    fstream file;
    ofstream output;
    file.open("D-large.in");
    output.open("answer.txt");

    int n=0;

    file>>n;


    for(int i=1;i<=n;i++)
    {
        int ele;
        file>>ele;

        vector<double> a,b;
        double temp;

        for(int i=0;i<ele;i++)
        {
            file>>temp;
            a.push_back(temp);
        }
        for(int i=0;i<ele;i++)
        {
            file>>temp;
            b.push_back(temp);
        }

        sort(a.begin(),a.end());
        sort(b.begin(),b.end());

        int first=war(a,b);
        int second=dec_war(a,b);

        //cout<<"Case #"<<i<<": "<<first<<" "<<second<<endl;
        output<<"Case #"<<i<<": "<<second<<" "<<first<<endl;
    }


}
