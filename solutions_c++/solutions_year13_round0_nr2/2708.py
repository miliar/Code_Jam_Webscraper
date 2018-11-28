#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

int main()
{
    int t,n,m;
    scanf("%d" , &t);
    int arr[101][101];
    int row[101];
    int col[101];
    int case_no =0;
    //FILE *f;
    //f= fopen("out.txt" , "w");
    while(t--)
    {
        case_no++;
        for(int x= 0 ; x< 101 ; x++)
        {
            row[x] = 0;
            col[x] = 0;
        }
        scanf("%d%d" , &n,&m);
        for(int i =0 ; i< n ; i++)
        {
            for(int j =0 ; j< m ; j++)
            {
                scanf("%d" , &arr[i][j]);
                if(arr[i][j] > row[i])
                {
                    row[i] = arr[i][j];
                }
                if(arr[i][j] > col[j])
                {
                    col[j] = arr[i][j];
                }
            }
        }
        int flag = 0;

        for(int i =0 ; i< n ; i++)
        {
            for(int j =0 ; j< m ; j++)
            {
                if(row[i]> arr[i][j] && col[j] > arr[i][j] )
                {
                    flag = 1;
                    break;
                }
            }
        }
        if(flag == 0)
        {
            printf( "Case #%d: YES\n" , case_no);
        }
        else
        {
            printf( "Case #%d: NO\n" , case_no);
        }

    }
    //fclose(f);
    return 0;
}
