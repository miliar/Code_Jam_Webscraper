#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void sovelout2(int &out, vector<float>& ken, vector<float>& nami)
{
    int k=0;
    for(int i=0; i<nami.size(); i++)
    {
        for(int j=k; j<ken.size(); j++)
        {
            k++;        
            if(ken[j]>nami[i])
            {
                out++;
                break;
            }
        }    
    }


}

int main(int argc, char** argv)
{
    FILE *file = fopen("tic.in","r"); 
    FILE *out = fopen("tic.out","w");
    int n=0;
    fscanf(file,"%d",&n);

    for(int i=0; i<n; ++i)
    {
        int k;
        fscanf(file,"%d",&k);
        fprintf(out,"Case #%d: ",i+1);
        vector<float> nami,ken;

        for(int j=0; j<k; j++)
        {
            float temp = 0;
            fscanf(file,"%f",&temp);
            ken.push_back(temp);
        }
       
        for(int j=0; j<k; j++)
        {
            float temp = 0;
            fscanf(file,"%f",&temp);
            nami.push_back(temp);
        }
        
        sort(ken.begin(),ken.end());
        sort(nami.begin(),nami.end());
        int out1=0,out2=0;
        sovelout2(out2,ken,nami);
        sovelout2(out1,nami,ken);
        fprintf(out,"%d %d\n",out2,k-out1);
    }

    fclose(file);
    fclose(out);
    return 0;
}
