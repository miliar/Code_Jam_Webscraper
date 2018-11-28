#include <iostream>
#include<cstring>
/*
English is a West Germanic language that was first spoken in ear
ly medieval England a
nd is now a global lingua franca.[4][5] English is either the o
fficial language or an official language in almost 60 sovereign states. It
 is the most commonly spoken language in the United Kingdom, the Unit
 ed States, Canada, Australia, Ireland, and New Zealand, and it is widely spok
 en in some areas of the Caribbean, Africa, and South Asia.[6] I
 t is the third most common native language in the world, after Mandarin and Spanish
 .[7] It is the most widely learned second language and is an official language of the
  United Nations, of the European Union, and of many other world and regional
   international organisations.

English has developed over the course of more than
 1,400 years. The earliest forms of English, a set of Anglo-Fr
 isian dialects brought to Great Britain by Anglo-Saxon 
 settlers in the fifth century, are called Old English. Middle 
 English began in the late 11th century with the Norman conquest 
 of England.[8] Early Modern English began in the 
 late 15th century with the introduction of the printing pre
 ss to London and the King James Bible as well as the Great Vowel 
 Shift.[9] Through the worldwide influence of the British 
 Empire, modern English spread around the world f
 rom the 17th to mid-20th centuries. Throu
 gh all types of printed and electronic 
 media, as well as the emergence of the United States as a global superp
 ower, English has become the leading language of international discourse
  and the lingua franca in many regions and in professional contexts su
  ch as science, navigation, and law.[10]

Modern English has little inflection compared with
 many other languages, and relies on auxiliary verbs
  and word order for the expression of complex tenses,
   aspect and mood, as well as passive constructions, int
   errogatives and some negation. Despite noticeable variatio
   n among the accents and dialects of English u
   sed in different countries and regions – in 
   terms of phonetics and phonology, and sometimes also
    vocabulary, grammar and spelling – English speakers fro
	m around the world are able to 
*/
long long int qzzz;
long long int yzz;
long long int ozzzzzzzzz;
long long int hzz;
long long int mzzzzz;
long long int yzzzzzz;
long long int ozzzzz;
long long int hzzz;
long long int z;

using namespace std;

string re(string sass,long long int i,long long int k)
{
    for(long long int pkl=i,ykl=k;ykl>=pkl;pkl++,ykl--)
    {
        if(pkl!=ykl)
        {
            if(sass[pkl]=='+')
                sass[pkl]='-';
            else
                sass[pkl]='+';
        }
        //this quest is good
         if(sass[ykl]=='+')
                sass[ykl]='-';
            else
                sass[ykl]='+';
                //love u codejam
        swap(sass[pkl],sass[ykl]);
    }
    // return string
    return sass;
}

int main()
{
    freopen("in.in","r",stdin);
	freopen("out.in","w",stdout);
 	//stdin to cin
 	//stdout to cout
 	//declaring testcase
    long long int testcase;
    //input testcase
    cin>>testcase;
    long long int cup= testcase;
    while(testcase--)
    {
        string karchi;
        //correct spelling of karchi is karchhi
        cin>>karchi;
        long long int lnt=karchi.size()-1;
        long long int coun=0;
        while(lnt>=0)
        {
            long long int k=lnt;
            while(karchi[k]=='+')
            {
                k--;
            }
            lnt=k;
            //lnt is length of string
            if(lnt>=0)
            {
                long long int i=0;
                while(karchi[i]=='+')
                {
                    i++;
                }
                if(i)
                {
                    karchi=re(karchi,0,i-1);
                    coun++;
                }
                karchi=re(karchi,0,lnt);
                coun++;
            }
        }
    cout<<"Case #"<<cup-testcase<<": "<<coun<<endl;
    }
return 0;
}
