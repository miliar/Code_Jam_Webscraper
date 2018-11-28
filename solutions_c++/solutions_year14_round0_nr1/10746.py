#include<fstream>
#include<iostream>

using namespace std;

int main()
{

    int T, soln1, soln2, arr1[4][4], arr2[4][4], flag=0, i, j, g, h, p, q;

    ifstream f1;

    f1.open("A-small-attempt1.in");
    f1>>T;

    int op[T], number[T];

    for(int c=0; c< T; ++c)
    {

        f1>>soln1;

        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                f1>>arr1[i][j];

        f1>>soln2;

        for(g=0; g<4;g++)
            for(h=0; h<4; h++)
                f1>>arr2[g][h];


        flag=0;

        for(p=0; p<4; p++)
            for(q=0; q<4; q++)


                if(arr1[soln1-1][p] == arr2[soln2-1][q])
                {

                    number[c]=arr1[soln1-1][p];
                    flag++;

                }




        if(flag==0)
           op[c]=-1;

        else if(flag==1)
           op[c]=1;

        else if(flag > 1)
           op[c]=0;




    ofstream f2;

    f2.open("Aout.out");



        for(int l=0; l<T; l++)

           switch(op[l])

           {

               case -1:

           f2<<"Case #"<<l+1<<": Volunteer cheated!"<<endl;
           break;

           case 0:

           f2<<"Case #"<<l+1<<": Bad magician!"<<endl;
           break;

           case 1:

           f2<<"Case #"<<l+1<<": "<<number[l]<<endl;
           break;

           }


       f2.close();

        }

f1.close();


return 0;

}



