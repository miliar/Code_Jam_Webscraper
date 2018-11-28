#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("data.txt");
ofstream fout("data.out");

double Naomi[1001], Ken[1001];

void swap(double &x,double &y)
{
    double tmp;
    tmp=x;
    x=y;
    y=tmp;
}

void qsort(double a[],int s,int t)
{
     if(s>=t)return;
     int i=s,j=t;
     double mid=a[(i+j)>>1];
     while(i<=j)
     {
         while(a[i]<mid)i++;
         while(a[j]>mid)j--;
         if(i<=j)
             swap(a[i++],a[j--]);
     }
    qsort(a,s,j);
    qsort(a,i,t);
}

void display(int N)
{

    qsort(Naomi,1,N);
    qsort(Ken,1,N);
    int r1,r2;
    int i,tmp1,tmp2;
    tmp1 = 1;
    tmp2 = 1;
    r1 = 0;
    while (1)
    {
        while (Naomi[tmp1]<Ken[tmp2]) {++tmp1;if (tmp1>=N) break;}
        if (Naomi[tmp1]>Ken[tmp2]) ++r1;
        if (tmp1>=N) break;
        ++tmp1; ++tmp2;
    }
        tmp1 = 1;
        tmp2 = 1;
        r2 = N;
        while (1)
        {
            while (Naomi[tmp1] > Ken[tmp2]) {++tmp2; if (tmp2 >= N) break;}

            if (Naomi[tmp1] < Ken[tmp2]) --r2;
            if (tmp2 >= N) break;

            ++tmp1; ++tmp2;

        }

    fout << r1 << ' ' << r2;

}

int main()
{
    int i,T,N,j;
    fin >> T;
    for (i = 1; i <= T; ++i)
    {
       fin >> N;
       for (j = 1; j <= N; ++j) fin >> Naomi[j];
       for (j = 1; j <= N; ++j) fin >> Ken[j];
       fout << "Case #" << i <<": ";
       display(N);
       fout << endl;
    }
    return 0;
}
