
#include <iostream>

#include <cstring>
#include<math.h>

using namespace std;

int last(int*arr,int n)
{
    int i = 0,location = -1 ;
    for(i=0;i<n;i++)
    {
        if(arr[i] == 0)
            location = i;
    }
  return location;

}

void flip(int *arr,int till)
{
    int i = 0;
    for(i=0;i<=till;i++)
    {
        if(arr[i] == 0)
            arr[i]=1;
        else arr[i]=0;
    }
}

int cnt(int *arr,int n)
{
    int index,total = 0;
    index = last(arr,n);
    while(index >= 0)
    {
        flip(arr,index);
        total++;
        index = last(arr,n);
    }
    return total;

}

int main()
{
    int n,qwe;
    cin>>n;
    for(qwe = 0;qwe<n;qwe++){
    char a[200];
    int i;
    cin>>a;

    int arr[strlen(a)];
    for(i = 0;i<strlen(a);i++)
    {

        if(a[i] =='-')
            arr[i]=0;
        else arr[i]=1;

    }



    int total = cnt(arr,strlen(a));
    cout << "Case #" << qwe+1 << ": " << total<< endl;



    }

}
