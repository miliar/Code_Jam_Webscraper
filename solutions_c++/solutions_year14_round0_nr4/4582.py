#include <iostream>
#include <fstream>

using namespace std;

void sort(double a[],int size)
{
    int i,j;
    double tmp;
    bool flag;
    for(i=1;i<size;i++){
        flag = false;
        for(j=0;j<size-1;j++)
            if(a[j+1]<a[j]){
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
                flag = true;
            }
        if(!flag) break;
    }
}

int main()
{
    ifstream infile("D-large.in");
    ofstream outfile("ans.txt");

    int t;
    int n;
    double N[1000],K[1000];
    int ans1,ans2;
    int flag1,flag2;

    infile>>t;
    for(int i=0;i<t;i++){

        infile>>n;
        for(int j=0;j<n;j++) infile>>N[j];
        for(int j=0;j<n;j++) infile>>K[j];
        sort(N,n);
        sort(K,n);

        flag1 = flag2 = 0;
        ans2 = 0;
        while(1){
            if(N[flag1]<K[flag2]){
                flag1++;
                flag2++;
                ans2++;
            }
            else
                flag2++;
            if(flag2==n){
                ans2 = n - ans2;
                break;
            }
        }

        flag1 = 0;
        ans1 = 0;
        while(1){
            flag2 = 1;
            for(int j=flag1;j<n;j++)
                if(N[j]<K[j-flag1]) flag2 = 0;
            if(flag2==1||flag1==n){
                ans1 = n - flag1;
                break;
            }
            else
                flag1++;
        }

        outfile<<"case #"<<i+1<<": ";
        outfile<<ans1<<' '<<ans2<<endl;

    }
    return 0;
}
