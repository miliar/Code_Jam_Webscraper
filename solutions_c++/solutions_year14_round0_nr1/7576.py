#include <iostream>
#include<fstream>
#include <vector>
#include <string>
#include <cstring>
#include<math.h>

/*#define __SMALL_DATASET__
#define __LARGE_DATASET__

#ifdef __SMALL_DATASET__
	const int l_size = 10,
		d_size = 25,
		n_size = 10;
#else
	const int l_size= 15,
		d_size = 5000,
		n_size = 500;
#endif
*/

using namespace std;

int main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small-output1.out");

    //ifstream fin("test.in");
    //ofstream fout("test.out");

    int t, cards1[4][4], cards2[4][4], test1, test2, j, i,k, arr[4], cnt=0, result, l;
    fin>>t;
    for(l=0;l<t;l++)
    {
        cnt=0;
        fin>>test1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>cards1[i][j];
                if(i==test1-1)
                    //{
                    arr[j]=cards1[i][j];
                    //cout<<arr[j]<<" ";}
            }
        }

        fin>>test2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>cards2[i][j];
                if(i==test2-1)
                {
                    for(k=0;k<4;k++)
                    {
                        if(cards2[i][j]==arr[k])
                        {
                            cnt++;
                            result=cards2[i][j];
                            cout<<"Result "<<result<<"\n";
                        }
                    }
                }
            }
            //cout<<"\n";
        }

        if(cnt==1)
            fout<<"Case #"<<l+1<<": "<<result<<"\n";
        else if(cnt<1)
            fout<<"Case #"<<l+1<<": Volunteer cheated!\n";
        else
            fout<<"Case #"<<l+1<<": Bad magician!\n";


    }

    return(0);

}

