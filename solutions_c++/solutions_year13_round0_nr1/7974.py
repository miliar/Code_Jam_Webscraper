#include<iostream>

using namespace std;

int sum(int mat[], int init, int diff)
{
    int i = init;
    int sum = 0;
    int j = 0;
    while(j<4)
    {
        sum+=mat[i];
        i+=diff;
        j++;
    }

    return sum;
}

char decide(int mat[], int size, int inc)
{
    if(sum(mat,1,1) == 29 || sum(mat,5,1) == 29 || sum(mat,9,1) == 29 || sum(mat,13,1) == 29 || sum(mat,1,4) == 29 ||
            sum(mat,2,4) == 29 || sum(mat,3,4) == 29 || sum(mat,4,4) == 29 || sum(mat,1,5) == 29 || sum(mat,4,3) == 29)
        return 'O';

    if(sum(mat,1,1) == 40 || sum(mat,5,1) == 40 || sum(mat,9,1) == 40 || sum(mat,13,1) == 40 || sum(mat,1,4) == 40 ||
            sum(mat,2,4) == 40 || sum(mat,3,4) == 40 || sum(mat,4,4) == 40 || sum(mat,1,5) == 40 || sum(mat,4,3) == 40)
        return 'O';


    if(sum(mat,1,1) == 299 || sum(mat,5,1) == 299 || sum(mat,9,1) == 299 || sum(mat,13,1) == 299 || sum(mat,1,4) == 299 ||
            sum(mat,2,4) == 299 || sum(mat,3,4) == 299 || sum(mat,4,4) == 299 || sum(mat,1,5) == 299 || sum(mat,4,3) == 299)
        return 'X';

    if(sum(mat,1,1) == 400 || sum(mat,5,1) == 400 || sum(mat,9,1) == 400 || sum(mat,13,1) == 400 || sum(mat,1,4) == 400 ||
            sum(mat,2,4) == 400 || sum(mat,3,4) == 400 || sum(mat,4,4) == 400 || sum(mat,1,5) == 400 || sum(mat,4,3) == 400)
        return 'X';


    if(inc)
        return 'I';
    else
        return 'D';

}
int main()
{
    int size = 0;
    int inc = 0;
    int i=0, j=0,k=0;
    char p;
    char ans;
    int mat[17];
    for(i=1;i<=16;i++)
        mat[i] = 0;
    cin >> size;
    //cout << "size is"<<size;
    //cin >>p;
    for(j=0;j<size;j++)
    {
        inc = 0;
        for(i=1;i<=16;i++)
        {
            cin >> p;
            if(p== '\n')
                cin >> p;
            if(p=='T')
                mat[i] = -1;
            else if(p == '.')
                inc = 1;
            else if(p=='X')
                mat[i] = 100;
            else if(p=='O')
                mat[i] = 10;
        }
        
        //cin >> p;
        //cin >> p;
        //for(k=1;k<=16;k++)
            //cout << " "<<mat[k] <<" ";

        ans = decide(mat,size,inc);
        if(ans == 'X' || ans =='O')
            cout << "Case #"<<j+1<<": "<<ans<<" won"<<endl;
        else if(ans == 'D')
            cout <<"Case #"<<j+1<<": Draw"<<endl;
        else if(ans == 'I')
            cout <<"Case #"<<j+1<<": Game has not completed"<<endl;
    }
}
