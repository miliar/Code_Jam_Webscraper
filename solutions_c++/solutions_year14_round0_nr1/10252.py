#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;
int done =0;
    fstream input;
    ofstream output;

void checker(int * rel1, int * rel2)
{
    bool found=false;
    int nums=0;
    bool mdo=false;
    int tell;
    cout<<done+1<< " check\n";
    for(int i=0; i<4;i++)
        {
            for (int j=0; j<4;j++)
                {

                        if (rel1[i]==rel2[j])
                        {
                              tell=rel1[i];
                            nums++;
                            found =true;
                        }
                }
        }
cout <<"Nums: "<< nums << endl;
        if (found ==true&& nums==1)
        {
             output<< "Case #" <<done+1<<": "<<tell<<"\n";
             done++;
        }
        else if(found ==true&& nums>1)
        {
            output<< "Case #" <<done+1<<":"<<" Bad magician!\n";
            done++;
        }
         else
        {
            output<< "Case #" <<done+1<<":"<<" Volunteer cheated!\n";
            done++;
        }
       nums =0;
return;
}

void cpy(int * src, int * dest)
{
    for (int i=0; i <4; i++)
    {
        dest[i] = src[i];
    }
    return;
}


void pr(int * arr)
{
    for (int i=0; i <4; i++)
    {
        output << arr[i]<<"   ";
    }
    output << endl;
}

int main()
{


    input.open("A-small-attempt3.in");
    //input.open("inTXT.in");
    output.open("ans.txt");
    int r1[4];
    int r2[4];
    int r3[4];
    int r4[4];
    int rel1[4];
    int rel2[4];
    int cases;
    int ans1,ans2;
    int tr[4];
    int temp;
    int a=0;
    input>>cases;
    int lim= cases;
    while(!input.eof())
    {
//        output<< cases <<endl;
        input>>ans1;

        // if(ans1 > 4){done++;cout<< "Case #" <<done<<": "<<" Volunteer cheated!\n"; continue;}

             for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r1[i]= temp;
                }
                a++;
                if(a == ans1) {cpy(r1, rel1);}


                for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r2[i]= temp;
                }
                a++;
                if(a==ans1){cpy(r2, rel1);}

                for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r3[i]= temp;
                }
                a++;
                if(a==ans1){cpy(r3, rel1);}

                for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r4[i]= temp;
                }
               a++;
               if(a==ans1){cpy(r4, rel1);}
//    output<<"aNS1: "<< ans1<<endl;
//    output<<"rel1: "<<endl;pr(rel1);

    input>> ans2;
    a=0;
                 for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r1[i]= temp;
                }
                a++;
                if(a == ans2) {cpy(r1, rel2);}


                for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r2[i]= temp;
                }
                a++;
                if(a == ans2) {cpy(r2, rel2);}

                for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r3[i]= temp;
                }
                a++;
               if(a == ans2) {cpy(r3, rel2);}

                for(int i=0;i<=3;i++)
                {
                    input>>temp;
                    r4[i]= temp;
                }
               a++;
               if(a == ans2) {cpy(r4, rel2);}
//           output<<"aNS2: "<< ans2<<endl;
//    output<<"rel2: "<<endl;pr(rel2);
    checker(rel1, rel2);
    a=0;

    if (lim== done)
    {
        break;
    }
    }


input.close();
output.close();
    return 0;
}
