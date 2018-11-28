#include<iostream>
#include<vector>
#include<array>
using namespace std;

int main()
{
    FILE* inputFile=fopen("A-small-attempt2.in.txt","r");
    FILE* outputFile=fopen("output.txt","a+");
    int iterator;
    fscanf(inputFile,"%d",&iterator);
    for(int ii=1;ii<=iterator;ii++)
    {
        cout<<ii<<endl;
        array<int,17> bitmap={};
        int answer1, answer2;
        fscanf(inputFile,"%d",&answer1);
        vector<int> matrix_1(16);
        for(int jj=0;jj<16;jj++)
            fscanf(inputFile,"%d",&matrix_1[jj]);
        
        fscanf(inputFile,"%d",&answer2);
        vector<int> matrix_2(16);
        for(int jj=0;jj<16;jj++)
            fscanf(inputFile,"%d",&matrix_2[jj]);
        int counter=0;
        int theOne;
        int a=4*(answer1-1);
        int b=4*answer1-1;
        for(int kk=a;kk<=b;kk++){
            bitmap[matrix_1[kk]]=1;
        }
        for(int jj=4*(answer2-1);jj<=4*answer2-1;jj++){
            if(bitmap[matrix_2[jj]]>0){
                counter++;
                theOne=matrix_2[jj];
            }
        }
        if(counter==0)
            fprintf(outputFile,"Case #%d: Volunteer cheated!\n",ii);
        else if(counter==1)
            fprintf(outputFile,"Case #%d: %d\n",ii,theOne);
        else if(counter>1)
            fprintf(outputFile,"Case #%d: Bad magician!\n",ii);
    }
    return 0;
}





