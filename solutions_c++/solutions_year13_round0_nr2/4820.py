#include <cstdio>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int strToInt(string s)
{
    return atoi(s.c_str());
}

void printArr(int m, int n, int arr[])
{
    for(int i = 0; i<m; i++)
    {
        for(int j = 0; j<n; j++)
        {
            cout << arr[i+m*j] << " ";
        }
        cout << endl;
    }
}

int main(int argc, char** args)
{
    ifstream file;
    file.open ("Blarge");

    string tmp = "";
    string token;
    getline( file, tmp );
    int T = atoi(tmp.c_str());

    for(int t = 0; t<T; t++)
    {
        getline( file, tmp );

        istringstream iss(tmp);
        getline(iss, token, ' ');
        int m = strToInt(token);
        getline(iss, token, ' ');
        int n = strToInt(token);

        int arr[n*m];

        for(int i = 0; i<m; i++)
        {
            getline(file, tmp);
            istringstream iss(tmp);
            for(int j = 0; j<n; j++)
            {
                getline(iss, token, ' ');
                arr[i+m*j] = strToInt(token);
            }
        }

        // Input handling done

        int hor[m*n];
        int ver[m*n];
        int max;

        // Find horz max
        for(int i = 0; i<m; i++)
        {
            max = 0;
            for(int j = 0; j<n; j++)
            {
                max = max<arr[i+m*j] ? arr[i+m*j] : max;
            }
            for(int j = 0; j<n; j++)
            {
                if(arr[i+m*j] == max) hor[i+m*j] = 1;
                else hor[i+m*j] = 0;
            }
        }

        // Find ver max
        for(int j = 0; j<n; j++)
        {
            max = 0;
            for(int i = 0; i<m; i++)
            {
                max = max<arr[i+m*j] ? arr[i+m*j] : max;
            }
            for(int i = 0; i<m; i++)
            {
                if(arr[i+m*j] == max) ver[i+m*j] = 1;
                else ver[i+m*j] = 0;
            }
        }

        /*
        printArr(m,n,arr);
        cout << endl;
        printArr(m,n,hor);
        cout << endl;
        printArr(m,n,ver);
        cout << endl;
        */

        // Test
        bool isOK = true;
        for(int i = 0; i<m && isOK; i++)
        {
            for(int j = 0; j<n; j++)
            {
                if(hor[i+m*j] + ver[i+m*j] == 0) {
                    isOK = false;
                    break;
                }
            }
        }

        if(isOK) printf("Case #%d: YES\n", t+1);
        else printf("Case #%d: NO\n", t+1);
    }
    //////////////////////////
}
