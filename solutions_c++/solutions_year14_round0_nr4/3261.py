#include<iostream>
#include<stdio.h>
#include<fstream>
#include<iomanip>

using namespace std;
void sorting(float arr[],int n)
{
    for(int x=0; x<n; x++)

	{

		int index_of_min = x;

		for(int y=x; y<n; y++)

		{

			if(arr[index_of_min]>arr[y])

			{

				index_of_min = y;

			}

		}

		double temp = arr[x];

		arr[x] = arr[index_of_min];

		arr[index_of_min] = temp;

	}
}
int main()
{
    ifstream fin;
    fstream fout;
    fin.open("input.txt",ios::in);
    fout.open("output.out",ios::out);
    int T=0;
    fin>>T;

    float nao[1000],ken[1000],diff;
    int i,j,N,used1[1000],used2[1000],v1,v2,flag,index;
    int used=0;
    for(int n=0;n<T;n++)
    {
       fin>>N;
       for(i=0;i<1000;i++) flag = used1[i] = used2[i]= nao[i]=ken[i]=0.0;
       for(i=0;i<N;i++) fin>>nao[i];
       for(i=0;i<N;i++) fin>>ken[i];
        sorting(nao,N);
        sorting(ken,N);

       v1 = v2 = 0;
       for(i=0;i<N;i++)
       {
           diff=0;
           flag=0;
            for(j=0;j<N;j++)
            {
                if(nao[i]>ken[j])
                {
                    if(used2[j]==0)
                    {
                        flag=1;
                        index=j;
                        break;
                    }
                }
            }
            if(flag==1)
            {
                used2[j]=1;
                v1++;
            }
       }
       for(i=0;i<N;i++)
       {
           diff=0;
           flag=0;
            for(j=0;j<N;j++)
            {
                if(ken[j]>nao[i])
                {
                    if(used1[j]==0)
                    {
                        flag=1;
                        index=j;
                        break;
                    }
                }
            }
            if(flag==1)
            {
                used1[j]=1;
                v2++;
            }
       }
        v2=N-v2;

        cout<<"Case #"<<n+1<<": "<<v1<<" "<<v2<<endl;
        fout<<"Case #"<<n+1<<": "<<v1<<" "<<v2<<endl;


    }
    return 0;
}
