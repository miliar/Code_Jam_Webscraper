#include<fstream>
#include<iostream>

using namespace std;

int main()
{

    int T, ans1, ans2, mat1[4][4], mat2[4][4], turn=0, i, j, g, h, p, q;

    ifstream f1;

    f1.open("A-small-attempt0.in");
    f1>>T;

    int output[T], num[T];

    for(int c=0; c< T; ++c)
    {

        f1>>ans1;

        for(i=0; i<4; ++i)
            for(j=0; j<4; ++j)
                f1>>mat1[i][j];

        f1>>ans2;

        for(g=0; g<4;++g)
            for(h=0; h<4; ++h)
                f1>>mat2[g][h];


        turn=0;

        for(p=0; p<4; ++p)
            for(q=0; q<4; ++q)


                if(mat1[ans1-1][p] == mat2[ans2-1][q])
                {

                    num[c]=mat1[ans1-1][p];
                    turn++;

                }




        if(turn==0)
           output[c]=-1;

        else if(turn==1)
           output[c]=1;

        else if(turn > 1)
           output[c]=0;




    ofstream f2;

    f2.open("Aout.out");



        for(int l=0; l<T; ++l)

           if(output[l]==-1)
               f2<<"Case #"<<l+1<<": Volunteer cheated!"<<endl;
           else if(output[l]==0)
               f2<<"Case #"<<l+1<<": Bad magician!"<<endl;
           else if(output[l]==1)
               f2<<"Case #"<<l+1<<": "<<num[l]<<endl;


       f2.close();

        }

f1.close();


return 0;

}



