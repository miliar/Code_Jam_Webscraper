#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

string strarr[101];
char idenstr[101];
int strnum[101][101];
bool flag;

int main()
{
    int T;
    cin >> T;
    for (int test=1; test<=T; test++)
    {
        int N;
        cin >>N;
        for (int i=0; i<N; i++)
        {
            cin >> strarr[i];
        }
        for (int i=0; i<N; i++)
            for (int j=0; j<101; j++)
                strnum[i][j]=0;

        idenstr[0] = strarr[0][0];
        strnum[0][0] = 1; 
        int k=1;
        int idenk=0;
        while (strarr[0][k]!='\0')
        {
            //cout << strarr[0][k] <<":" <<idenstr[idenk]<< endl;
            if (strarr[0][k]==idenstr[idenk])
                strnum[0][idenk]++;
            else
            {
                idenk++;
                idenstr[idenk]=strarr[0][k];
                strnum[0][idenk]++;
            }
            k++;
        }
        int idenN=idenk+1;
        flag = true;
        for (int i=1; i<N; i++)
        {
            k=0;
            idenk=0;
            while (strarr[i][k]!='\0')
            {
                if (strarr[i][k]==idenstr[idenk])
                    strnum[i][idenk]++;
                else
                {
                    idenk++;
                    if (strarr[i][k]==idenstr[idenk])
                        strnum[i][idenk]++;
                    else
                    {
                        flag = false;
                        break;}
                }
                k++;
            }
            if (!flag)
                break;
        }
        /*for (int i=0; i<N; i++)
        {
            for (int j=0; j<idenN; j++)
            {
                cout << strnum[i][j];
            }
            cout <<endl;
        }*/
        if (flag)
        {
            int min=0;
            for (int j=0; j<idenN; j++)
            {
                double sum =0;
                for (int i=0; i<N; i++)
                {
                    if (strnum[i][j]==0)
                    {
                        flag = false;
                        break;
                    }
                    sum+=double(strnum[i][j]);
                }
                if (!flag)
                    break;
                sum = sum/double(N);
                int iden = int(sum+0.5);
                for (int i=0; i<N; i++)
                    min+=abs(strnum[i][j]-iden);
            }
            if (flag)
                cout <<"Case #" << test << ": "<< min <<endl;
        }
        if (!flag)
            cout <<"Case #" << test << ": Fegla Won" << endl;
    }
}
