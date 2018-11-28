#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;

bool isVowel(char c){
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
        return true;
    return false;
}

bool hasNConVowels(char *st, int n){
    int l = strlen(st);
    for(int i=0,j; i<=l-n; i++){
        for(j=0; j<n; j++)
            if(isVowel(st[i+j]))
                break;
        if(j==n)
            return true;
    }
    return false;
}
char *substring(char *string, int position, int length)
{
   char *pointer;
   int c;

   pointer = (char*)malloc(length+1);

   if (pointer == NULL)
   {
      printf("Unable to allocate memory.\n");
      exit(EXIT_FAILURE);
   }

   for (c = 0 ; c < position -1 ; c++)
      string++;

   for (c = 0 ; c < length ; c++)
   {
      *(pointer+c) = *string;
      string++;
   }

   *(pointer+c) = '\0';

   return pointer;
}
int countN(char *string, int n){
    char *pointer;
    int position = 1, length = 1, temp, string_length;
    int count = 0;
   temp = string_length = strlen(string);

   while (position <= string_length)
   {
      while (length <= temp)
      {
         pointer = substring(string, position, length);
        //cout<<pointer<<endl;
         bool f = hasNConVowels(pointer,n);
         if(f)
            count++;
         length++;
      }
      temp--;
      position++;
      length = 1;
   }

    return count;
}

int main(){
    ifstream in("A-small.in");
    ofstream out("A-small.out");

    int cases, t = 1;
    in>>cases;
    //cout<<cases<<endl;
    while(t <= cases){
        char name[101];
        int n;
        in>>name;
        in>>n;
        int s = countN(name,n);
        out<<"Case #"<<t<<": "<<s<<endl;
        t++;
    }
    in.close();
    out.close();
}
