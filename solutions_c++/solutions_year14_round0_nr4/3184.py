#include <iostream>
#include <fstream>

using namespace std;

int Partition(float a[], int beg, int end)
{
int p=beg, loc;
float pivot=a[beg];
for(loc=beg+1;loc<=end;loc++)
{
if(pivot>a[loc])
{
a[p]=a[loc];
a[loc]=a[p+1];
a[p+1]=pivot;
p=p+1;
}
}
return p;
}

void QuickSort(float a[], int beg, int end)
{
if(beg<end)
{
float p=Partition(a,beg,end);

QuickSort(a,beg,p-1);
QuickSort(a,p+1,end);
}
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("D-large.in");
    fout.open("op3.txt");
    int tc, n, i, j, k, l, c1, c2, cv=0;
    float a[1000], b[1000];
    fin>>tc;
    while(tc--)
    {
        c1=0, c2=0, cv++;
        fin>>n;
        for(i=0;i<n;i++)
            fin>>a[i];
        for(i=0;i<n;i++)
            fin>>b[i];
        QuickSort(a, 0, n-1);
        QuickSort(b, 0, n-1);

        j=0; l=n-1, k=n-1;
        for(i=0;i<n;i++){
            if(a[i]>b[j]){c1++; j++;}
            if(a[k]<b[l]){c2++;l--;}
            k--;}

        fout<<"Case #"<<cv<<": "<<c1<<" "<<n-c2<<endl;

}

    return 0;
}
