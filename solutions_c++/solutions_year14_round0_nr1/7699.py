#include<iostream>
using namespace std;

void printarr(int a[], int n)
{
    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
    cout<<endl;
}

int contains(int b[], int a[], int &result)
{
    int count=0;
    
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            if(a[i]==b[j])
            {
                result = a[i];
                count++;
            }
    }
    return count;
}


int main()
{
    int T;
    freopen("A-small-attempt1.in", "r", stdin);
	freopen("result.out", "w", stdout);
    cin>>T;
    int first[16];
    int second[16];
    int firstrow[4];
    int secondrow[4];

    int result,temp;
    int row,row2;
    for(int k=1;k<=T;k++)
    {
        cin>>row;
        for(int i=0;i<16;i++)
        {
            cin>>first[i];
            if(i<4*row && i>=(row-1)*4)
                firstrow[i%4] = first[i];
        }
        cin>>row2;
        for(int i=0;i<16;i++)
        {
            cin>>second[i];
            if(i<4*row2 && i>=(row2-1)*4)
                secondrow[i%4] = second[i];
        }
        temp = contains(secondrow, firstrow, result);
        if(temp<=0)
            printf("Case #%d: Volunteer cheated!\n", k);
        else if(temp==1)
            printf("Case #%d: %d\n",k, result);
        else
            printf("Case #%d: Bad magician!\n", k);
        
    }

}
