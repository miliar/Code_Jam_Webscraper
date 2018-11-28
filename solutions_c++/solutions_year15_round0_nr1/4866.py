#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;
int main(int argc, char **argv) {
    ifstream in (argv[1]);
    ofstream out (argv[2]);
    int noOfcases;
    string row;
    const char *str;
    char maxShystr[5];
    int maxShyness=1000;
    int shyArr[1001];
    int count=0;
    int noOfFriends=0;
    int totalStanding=0;
    int j=0;

    getline(in, row);
    noOfcases=atoi(row.c_str());
    for(int i=1;i<=noOfcases;i++)
    {
        /* Initialize the variables */
        count=0;
        noOfFriends=0;
        totalStanding=0;
        for(j=0;j<5;j++) maxShystr[j]=0;
        for(j=0;j<=maxShyness;j++)
            shyArr[j] = 0;
        /* Read the first Arrangement */
        getline(in, row);
        str = row.c_str();
        /* Get Max Shyness */
        for(j=0;j<5;j++)
        {
            if (str[j] == ' ') break;
            maxShystr[j] = str[j];
        }
        maxShystr[j++] = 0;
        maxShyness = atoi(maxShystr);
        cout<<"Max Shyness"<<maxShyness<<"  ";
        for(;j<row.length();j++)
        {
            shyArr[count] = str[j]-'0';
            count++;
        }
        for(int j=0;j<=maxShyness;j++)
            cout<<shyArr[j]<<" ";
        /* Find the Number of Friends Required logic */
        totalStanding += shyArr[0];
        for(int j=1;j<=maxShyness;j++)
        {
            if (shyArr[j]>0)
            {
                if (totalStanding>=j)
                    totalStanding += shyArr[j];
                else{
                 /* Find No of Friends required to invite to make these persons to stand*/
                 noOfFriends += (j-totalStanding);
                 totalStanding = j+shyArr[j];
                }
            }
        }
        cout<<"Case #"<<i<<": "<<noOfFriends<<endl;
        out<<"Case #"<<i<<": "<<noOfFriends<<endl;
    }

}
