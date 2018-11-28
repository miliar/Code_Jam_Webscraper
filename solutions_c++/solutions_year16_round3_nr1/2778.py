#include<bits/stdc++.h>
using namespace std;

int a[100],b[100];


int main(){
FILE *fin1 = freopen("input.txt", "r", stdin);
FILE *fin2 = freopen("output.txt", "w", stdout);

int i,j,k,t,n,sum=0,max1=0, max2=0,ind1=0, ind2=0;
cin>>t;
int c=0;
    while(c<t){
        max1=0; max2=0;
        sum=0;
        c++;
        cout<<"Case #"<<c<<": ";

        cin>>n;
        for( i=0;i<2;i++){
            cin>>a[i];
            b[i]=a[i];
            sum+=a[i];
            if(i==0){
                max1=a[i];
                }
            if(i==1)
                max2=a[i];

        }
        ind1=0;
        ind2=1;
        if(max2>max1)
        {
            int temp;
            temp=max1;
            max1=max2;
            max2=max1;

            temp=ind1;
            ind1=ind2;
            ind2=temp;

        }

        for( i=2;i<n;i++){
            cin>>a[i];
            //b[i]=a[i];
            sum+=a[i];
            if(a[i]>max1){
                max2=max1;
                ind2=ind1;
                max1=a[i];
                ind1=i;
            }
            else if(a[i]<=max1 && a[i]>max2)
            {
                max2=a[i];
                ind2=i;
            }

        }
        while(1){
        //cout<<"m1  m2 "<<max1<<"  "<<max2<<endl;
        //cout<<"sum= "<<sum<<endl;
        //cout<<"ind1 ind2"<<ind1<<" "<<ind2<<endl;
            if(sum<=0)
            break;

            sum--;
            printf("%c", 65+ind1);
            a[ind1]--;

            int sum2;
            sum2=sum-1;

            if(sum2==0)
            {
                sum--;
                printf("%c ", 65+ind2);
                a[ind2]--;
            }
            else{
            for(j=0;j<n;j++){

                    if(a[j]>0 && j!=ind2 && j!=ind1 &&  ((sum2/2)<a[j]) ){
                        break;
                    }
            }
            if(j==n)
            {
                if(max1-1>=max2)
                {
                    printf("%c ", 65+ind1);
                    a[ind1]--;
                }
                else{
                printf("%c ", 65+ind2);
                a[ind2]--;}
                sum--;

            }
            else{
            cout<<" ";

            }

            }

            ////////////////////
        //cout<<"\na[i]= ";
        //for( i=0;i<n;i++){
        //    cout<<a[i]<<" ";
        //}

         max1=a[0];
          max2=a[1];
        ind1=0;
        ind2=1;
        if(max2>max1)
        {
            int temp;
            temp=max1;
            max1=max2;
            max2=temp;

            temp=ind1;
            ind1=ind2;
            ind2=temp;

        }

        for( i=2;i<n;i++){
 //cout<<"\n here1 ";
            if(a[i]>max1){
                max2=max1;
                ind2=ind1;

                max1=a[i];
                ind1=i;
   //          cout<<" here2 ";
            }
            else if(a[i]<=max1 && a[i]>max2)
            {
     //           cout<<" here3 ";
                max2=a[i];
                ind2=i;
            }

        }

    }

        cout<<endl;
    }


return 0;
}
