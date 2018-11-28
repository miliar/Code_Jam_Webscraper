/* 
 * File:   main.cpp
 * Author: Parnami
 * Created on April 12, 2014, 5:14 PM
 * Description : Google Code Jam 2014 Qualification Round. Question 4
 */

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

int main() {

    int t,l,r,c,m,n,numEmpty,i,j,sNaomi,eNaomi,sKen,maxKen,winNaomi,winKen,winNaomi2,winKen2,eKen;
    vector <double> naomi(1000),naomiCopy(1000),ken(1000),kenCopy(1000),validNaomi(1000),validKen(1000);
    ifstream input_data("D-large.in");
    ofstream outputFile("outterLarge.txt");
    input_data>>t;
    for(l=0;l<t;l++)
    {
        input_data>>n;
        naomi.clear();
        naomiCopy.clear();
        ken.clear();
        kenCopy.clear();
        validKen.clear();
        validNaomi.clear();
        naomi.resize(n);
        naomiCopy.resize(n);
        ken.resize(n);
        kenCopy.resize(n);
        validKen.resize(n);
        validNaomi.resize(n);
        winNaomi=0;
        winKen=0;
        winNaomi2=0;
        winKen2=0;
        for(i=0;i<n;i++)
        {
            input_data>>naomi[i];
            validNaomi[i]=1;
        }
        for(i=0;i<n;i++)
        {
            input_data>>ken[i];
            validKen[i]=1;
        }
        //cout<<"Input Done"<<endl;
        sort(naomi.begin(),naomi.begin()+n);
        sort(ken.begin(),ken.begin()+n);
        naomiCopy = naomi;
        kenCopy = ken;
        sNaomi = 0;
        eNaomi = n-1;
        sKen = 0;
        maxKen = n-1;
        //cout<<"Looping now"<<endl;
        for(i=n-1;i>=0;i--)
        {
            //cout<<naomi[i]<<endl;
            if(naomi[i]>ken[maxKen])
            {
                //cout<<"Naomi ki jeet"<<endl;
                validKen[sKen]=0;
                sKen++;
                while(validKen[maxKen]==0 && maxKen!=-1)
                                maxKen--;
                winNaomi++;
            }
            else
            {
                for(j=0;j<n;j++)
                {
                    if(ken[j]>naomi[i] && validKen[j]==1)
                    {
                        //cout<<"Ken ki jeet"<<endl;
                        winKen++;
                        validKen[j]=0;
                        while(validKen[maxKen]==0 && maxKen!=-1)
                                maxKen--;
                        break;
                    }
                }
            }
        }
        ken = kenCopy;
        naomi = naomiCopy;
        for(i=0;i<n;i++)
        {
            validKen[i]=1;
        }
        //cout<<"Ken : "<<winKen<<" Naomi : "<<winNaomi<<endl;
        sKen = 0;
        eKen = n-1;
        sNaomi = 0;
        eNaomi = n-1;
        //cout<<"Looping now"<<endl;
        for(i=n-1;i>=0;i--)
        {
            //cout<<naomi[i]<<endl;
            if(ken[i]>naomi[eNaomi])
            {
                //cout<<"Naomi ki jeet"<<endl;
                validNaomi[sNaomi]=0;
                sNaomi++;
                while(validNaomi[eNaomi]==0 && eNaomi!=-1)
                                eNaomi--;
                winKen2++;
            }
            else
            {
                for(j=0;j<n;j++)
                {
                    if(naomi[j]>ken[i] && validNaomi[j]==1)
                    {
                        //cout<<"Ken ki jeet"<<endl;
                        winNaomi2++;
                        validNaomi[j]=0;
                        while(validNaomi[eNaomi]==0 && eNaomi!=-1)
                                eNaomi--;
                        break;
                    }
                }
            }
        }
        //cout<<"Ken : "<<winKen2<<" Naomi : "<<winNaomi2<<endl;
        outputFile<<"Case #"<<l+1<<": "<<winNaomi2<<" "<<winNaomi<<endl;
    }
    return 0;
}

