#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    FILE *file;
    file = fopen("file.txt","a+");

    int T,i,j,k;
    int a,b,value,counter;
    int arrA[4][4];
    int arrB[4][4];

    cin>>T;
    for(i=0; i<T; i++)
    {
        counter=0;
        cin>>a;
        for(j=0; j<4; j++)
        {
            for(k=0; k<4; k++)
            {
                cin>>arrA[j][k];
            }
        }

        cin>>b;
        for(j=0; j<4; j++)
        {
            for(k=0; k<4; k++)
            {
                cin>>arrB[j][k];
            }
        }

        for(j=0; j<4; j++)
        {
            for(k=0; k<4; k++)
            {
                if(arrA[a-1][j]==arrB[b-1][k])
                {
                    value = arrA[a-1][j];
                    counter++;
                }
            }
        }

        if(counter==0)
            //cout<<"Case #" <<i+1 <<": Volunteer cheated!" <<endl;
            fprintf(file, "Case #%d: Volunteer cheated!\n", i+1);
        else if(counter==1)
            //cout<<"Case #" <<i+1 <<": " <<value <<endl;
            fprintf(file, "Case #%d: %d\n", i+1, value);
        else
            //cout<<"Case #" <<i+1 <<": Bad magician!" <<endl;
            fprintf(file, "Case #%d: Bad magician!\n", i+1);
    }
    //fprintf(file,"%s","This is just an example :)"); /*writes*/

    fclose(file); /*done!*/
    getchar(); /* pause and wait for key */

    return 0;
}
