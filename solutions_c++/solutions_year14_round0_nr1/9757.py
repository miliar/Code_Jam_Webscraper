#include<iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int c[220];
    int index = 0;
    for(int map = 0 ; map < t ; map++)
    {
        int a[4][4],b[4][4];
        int n1,n2;
        cin >> n1;
        for(int i = 0 ; i < 4 ; i++)
        {
            for(int j = 0 ; j < 4 ; j++)
            {
                cin >> a[i][j];
            }
        }
        cin >> n2;
        for(int i = 0 ; i < 4 ; i++)
        {
            for(int j = 0 ; j < 4 ; j++)
            {
                cin >> b[i][j];
            }
        }
        int counter = 0;
        int p=0;
        for(int i = 0 ; i < 4 ; i++)
        {
            for(int j = 0 ; j < 4 ; j++)
            {
                if(a[n1-1][i] == b[n2-1][j])
                {
                    p = i;
                    counter++;
                }
            }
        }
        //cout << "\n\n\n" << counter << "\n\n\n";
        c[index++] = counter;
        if(counter == 1)
        {
            c[index++] = a[n1-1][p];
        }
        else
        {
            c[index++] = 786;
        }
    }
    for(int i = 0 ; i < index ; i=i+2)
    {
        if(c[i] == 1)
        {
            cout << "Case #" << (i+1+1)/2 << ":" << " " << c[i+1] << "\n";
        }
        else if(c[i] > 1)
        {
            cout << "Case #" << (i+1+1)/2 << ":" << " " << "Bad magician!" << "\n";
        }
        else if(c[i] == 0)
        {
            cout << "Case #" << (i+1+1)/2 << ":" << " " << "Volunteer cheated!" << "\n";
        }
    }
    return 0;
}
