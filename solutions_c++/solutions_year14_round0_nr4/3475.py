#include <iostream>
#include<cstdio>
#define MAX 1100
using namespace std;

void swap(double &a,double &b)
{
	double temp=a;
	a=b;
	b=temp;
}

int partition(double arr[],int left,int right)
{
	double pivot=arr[left];
	int l=left+1,r=right;
	while(l<r)
	{
		while(arr[r]>pivot&&r>l)	r--;
		while(arr[l]<pivot&&l<r)	l++;
		if(l==r)
			break;
		swap(arr[r],arr[l]);
	}
	if(pivot<arr[l])
		l--;
	swap(arr[l],arr[left]);
	return l;
}

void sort(double arr[],int l,int r)
{
	if(l<r)
	{
		int pos=partition(arr,l,r);
		sort(arr,l,pos-1);
		sort(arr,pos+1,r);
	}
}

int DecitfulWar(double Naomi[],double Ken[],int N)
{
    int counter=0;
    int i=N-1,j=N-1;


    while(i>=0&&j>=0)
    {

        if(Naomi[i]>Ken[j])
        {
            counter++;
            j--;
            i--;
        }
        else
        {
            j--;
        }
    }
    return counter;
}

int War(double Naomi[],double Ken[],int N)
{
    int i=0,j=0;
    int counter=0;
    while(j<N)
    {
        if(Naomi[i]<Ken[j])
        {
            counter++;
            i++;
            j++;
        }
        else
            j++;
    }
    return (N-counter);
}
int main()
{

    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t;
    int c=1;
    cin>>t;
    while(t--)
    {
        int N;
        int i;
        cin>>N;
        double Naomi[MAX];
        double Ken[MAX];
        for(i=0; i<N; i++)
        {
            cin>>Naomi[i];
        }
        sort(Naomi,0,N-1);
        for(i=0; i<N; i++)
        {
            cin>>Ken[i];
        }

        sort(Ken,0,N-1);

        int a= DecitfulWar(Naomi,Ken, N);
        int b = War(Naomi,Ken, N);
        cout<<"Case #"<<c<<": "<<a<<" "<<b<<"\n";
        c++;
    }
    return 0;
}
