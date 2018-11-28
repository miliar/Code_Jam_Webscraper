#include <iostream>
using namespace std;
bool isSubset(int arr1[], int arr2[], int m, int n)
{
    int i = 0;
    int j = 0;
    for (i=0; i<n; i++)
    {
        for (j = 0; j<m; j++)
        {
           if(arr2[i] == arr1[j])
              break;
        }

        if (j == m)
           return 0;
    }
  
    return 1;
}

int main()
{
    int t,r=0,a=1,n,k[999],x=0,arr[10]={0,1,2,3,4,5,6,7,8,9};
    for(int i=0;i<999;i++){
      k[i]=12;
  }
  cin>>t;
  for(int l=1;l<=t;l++){
  	cin>>n;
  	if(n==0){
  		cout<<"Case #"<<l<<": INSOMNIA"<<"\n";
  	}
  	else{
        while(1){
            int t=n*a;
            int j=t;
            while(j>0){
                k[x]=j%10;
                j /= 10;
                x++;
            }
            
         int m = sizeof(k)/sizeof(k[0]);
           
        
       if(isSubset(k, arr, m, 10))
        {
        cout<<"Case #"<<l<<": "<<t<<"\n";
           break;
    }
        a++;}}
  a=1;x=0;
  for(int i=0;i<999;i++){
      k[i]=12;
  }
  }}