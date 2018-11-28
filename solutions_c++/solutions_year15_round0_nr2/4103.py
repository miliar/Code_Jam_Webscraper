#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int min(int a,int b)
{
    if(a>b)
        return b;
    return a;
}

int min1(int w,int x,int y)
{
    int m=w;
    if(x<m)
        m=x;
    if(y<m)
        m=y;
    return m;
}

int divide(vector<int>&a,int &max,int def)
{
    int c=0;
    if(def==0)
        return 0;
    if(def>=max){
        max=1;
        return 0;
    }
    for(int i=0;i<a.size();i++){
        if(a[i]==max){
            a.push_back(def);
            a.push_back(a[i]-def);
            a.erase(a.begin()+i);
            i--;
            c++;
        }
    }
    return c;
}


int nc(vector <int> a,int max,int def)
{
    if(max<=1)
        return 1;
    int c=divide(a,max,def);
    int max1=0;
    for(int i=0;i<a.size();i++)
        if(a[i]>max1)
            max1=a[i];
    if(max!=1)
        return min(c+max1,c+min1(nc(a,max1,2),nc(a,max1,3),nc(a,max1,4)));
    else
        return c+max1;
}

	main()
	{
    ifstream in("B-small-attempt0.in");
    ofstream out("output.txt");
    int t;
    in>>t;
    int kk=1;
    while(kk<=t)
		{
        vector<int> v;
        int No,te,max=0;
        in>>No;
        for(int i=0;i<No;i++){
            in>>te;
            if(max<te)
                max=te;
            v.push_back(te);
        }
        out<<"Case #"<<kk<<": "<<min(max,nc(v,max,0))<<endl;
    kk++;
	}

}
