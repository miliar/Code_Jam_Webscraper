#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#define sqr(x) (x)*(x)

template <class T>
class Array2D
{
    T**    strings;
    int*   lengths;
    int    numElem;
    int    allocated;
    
    public:
           
    Array2D()
    {
        numElem = 0;
        strings = new T*[50];
        lengths = new int[50];
        allocated = 50;
    }
    
    bool add(T* str,unsigned int len)      
    {
        int i;
        if (numElem == allocated)
        {
            T** stringsNew = new T*[allocated+50];
            int* lengthsNew = new int[allocated+50];
            if (stringsNew == NULL)
            {
                printf("BAJ VAN");
                return false;
            }
            for (i=0; i<allocated; i++)
            {
                stringsNew[i] = strings[i];
                lengthsNew[i] = lengths[i];
            } 
            allocated = allocated + 50;
            delete[] strings;
            delete[] lengths;
            strings = stringsNew;
            lengths = lengthsNew;
            //printf("%d %s | ",allocated,strings[0]);
        }
        strings[numElem] = new T[len];
        lengths[numElem] = len;
        for (i=0; i<len; i++)
        {
            strings[numElem][i] = str[i];
        }
        //printf("added: %d\r\n",strings[numElem][0]);
        numElem++;
        return true;
    }
    
    T* get(int i)
    {
        return strings[i];      
    }
    
    int length(int i)
    {
        return lengths[i];    
    }
    
    int find(T* str)
    {
        int i,i2;
        for (i=0; i<numElem; i++)
        {
            for (i2 = 0; strings[i][i2] == str[i2] && str[i2] && strings[i][i2] ; i2++);
            if (str[i2] == '\0' && strings[i][i2] == '\0')
                return i+1;
        }
        return 0;
    }
    
    int clear()
    {
        int i;
        for (i = 0; i<numElem; i++)
        {
            delete[] strings[i];
        }    
        delete[] strings;
        delete[] lengths;
        
        numElem = 0;
        strings = new T*[50];
        lengths = new int[50];
        allocated = 50;
    }
    
    ~Array2D()
    {
        int i;
        for (i = 0; i<numElem; i++)
        {
            delete[] strings[i];
        }    
        delete[] strings;
        delete[] lengths;
    }
};

class StringArray: public Array2D<char>
{
  public:
    StringArray():Array2D<char>()
    {}     
         
    bool add(char* str)
    {
        return Array2D<char>::add(str,strlen(str)+1);          
    }      
};

class FileManager
{
    char* filename;
    FILE* f;
    
    int testcases;
    
  public:
         
    FileManager()
    {
        filename = new char[50];
        f = NULL;             
    }
    
    FILE* getPointer()
    {
    	return f;
    }
         
    bool open2read(const char* fname)
    {
        strcpy(filename,fname);    
        f = fopen((const char*)filename,"r");
        if (f == NULL)
           return false;
        return true;
    }

    bool open2write(const char* fname)
    {
        strcpy(filename,fname);    
        f = fopen((const char*)filename,"w");
        if (f == NULL)
           return false;
        return true;
    }
    
    bool close()
    {
        fclose(f);
        return true;
    }
    
    int readArray(int *array)
    {
        int  num = 0;
        char c = ' ';
        
        for (num=0; num<5 && c!='\r' && c!='\n'; num++)
        {
            if (fscanf(f,"%d%c",&array[num],&c) != 2) break;
        }
        
        return num;
    }
    
    int readArray(double *array)
    {
        int  num = 0;
        char c = ' ';
        
        for (num=0; num<5 && c!='\r' && c!='\n'; num++)
        {
            if (fscanf(f,"%lf%c",&array[num],&c) != 2) break;
        }
        
        return num;
    }
        
    bool readString(char* str, int n)
    {
         if (fgets(str,n,f) != NULL)
         {
             int size = strlen(str);
             if (size > 0 && (str[size-1] == '\r' || str[size-1] == '\n')) 
                 str[size-1] = '\0';
             if (size > 1 && (str[size-2] == '\r' || str[size-2] == '\n')) 
                 str[size-2] = '\0';
             return true;
         }
         return false;
    }
    
    bool readNum(int* pnum)
    {
         if (fscanf(f,"%d",pnum) > 0)  
             return true;
         return false;
    }
    
    bool writeResult(int * result,int n)
    {
         for (int i=0; i<n; i++)
         {
             fprintf(f,"Case #%d: %d\n",i+1,result[i]);    
         }
    }     

    bool writeResult(Array2D<int>& result,int n)
    {
         int *array,num;
         for (int i=0; i<n; i++)
         {
             fprintf(f,"Case #%d: ",i+1);
             array = result.get(i);
             num   = result.length(i);
             for (int i2 = 0; i2 < num; i2++)
                 fprintf(f,"%d ",array[i2]);
             fprintf(f,"\n");    
         }
    }     

    bool writeResult(StringArray& result,int n)
    {
         for (int i=0; i<n; i++)
         {
             fprintf(f,"Case #%d: %s\n",i+1,result.get(i));    
         }
    }     
    
    ~FileManager()
    {
        if (f != NULL)
        fclose(f);              
    }
};

int main()
{
     FileManager     input,output;
     int header[10];
     Array2D<int>    dataset;
     //Array2D<long>   dataset;
     //Array2D<double> dataset;
     //StringArray     dataset;
     int testcases;
     Array2D<int>    result;
     //Array2D<long>   result;
     //Array2D<double> result;
     //StringArray     result;
     
     
     printf("START");
     
     int temp[500],N,M,K,all,border,border3,bordermin,c1,c2,row,col,empty,lastborder,lastborder3,lastall;
     int border2,border1,lastborder2,lastborder1;
     double row0, col0, rad, radsqr, rowoffset, coloffset, lastradsqr;
     bool full;

 	 if (!input.open2read("input.txt")) printf("error at file opening!");
     input.readArray(header);
     testcases = header[0];
     for (int i=0; i<testcases; i++)
     {
         input.readArray(temp);
         N = temp[0];
         M = temp[1];
         K = temp[2];
         row0 = (N-1)/2;
         col0 = (M-1)/2;
         bordermin = N*M;
         
         if (K<5 || N==1 || M==1) {result.add(&K,1); continue; }
         if (K == (N*M)) { border = N*2 + (M-2)*2;  result.add(&border,1); continue; }
         
         //rowoffset = row0-floor(row0); 
         //coloffset = row0-floor(row0); 
         for (row0 = (N-1)/2.0; row0 < N/2.0+0.1; row0+=0.5)
         {
             for (col0 = (M-1)/2.0; col0 < M/2.0+0.1; col0+=0.5)
             {
                 for (c1=0;c1<1000;c1++)
                 {
                     for (c2=0;c2<=c1;c2++)
                     {
                         radsqr = sqr(c1+row0-floor(row0)) + sqr(c2+col0-floor(col0));
                         all = 0;
                         border = 0;
                         border3 = 0;
                         border2 = 0;
                         border1 = 0;
                         full = false;
                         for (row = 0; row < N ; row++)
                         {
                             for (col = 0; col < M ; col++)
                             {
                                 if ((sqr(row-row0) + sqr(col-col0)) <= radsqr) all++;
                                 if ((sqr(row-row0) + sqr(col-col0)) <= radsqr)
                                 { 
                                    if(row == 0 || row == (N-1) || col == 0 || col == (M-1)) 
                                        border++;
                                    else
                                    {
                                        empty = 0; 
                                        if ((sqr(row-row0+1) + sqr(col-col0)) > radsqr) empty++;
                                        if ((sqr(row-row0-1) + sqr(col-col0)) > radsqr) empty++;
                                        if ((sqr(row-row0) + sqr(col-col0+1)) > radsqr) empty++;
                                        if ((sqr(row-row0) + sqr(col-col0-1)) > radsqr) empty++;
                                        if (empty > 0) border++;
                                        if (empty == 1) border3++;
                                        if (empty == 2) border2++;
                                        if (empty == 3) border1++;
                                    }    
                                 }
                                 if (all > K) { full=true; break; }
                             }
                             if (full) break;
                         }
                         if (full) break;
                         else
                         {
                            lastradsqr = radsqr;
                            lastborder = border;
                            lastborder3 = border3;
                            lastborder2 = border2;
                            lastborder1 = border1;
                            lastall = all;
                         }
                     }
                     if (full) break;
                 }
                 //if ((K-lastall) > lastborder3) lastborder += ((K-lastall) - lastborder3);
                 while (K>lastall)
                 {
                     if (lastborder3>0) { lastall+=1; lastborder+=0; lastborder3-=1; }
                     else
                     if (lastborder2>1) { lastall+=2; lastborder+=1; lastborder2-=2; }      
                     else
                     if (lastborder3>2) { lastall+=3; lastborder+=2; lastborder3-=3; }
                     else
                     { lastall++; lastborder++; }      
                 }
                 if (lastborder < bordermin) bordermin = lastborder;

                 if (i==3)
                 {
                          printf("%dx%d-%d\r\n",N,M,K);
                 radsqr = lastradsqr;
                 for (row = 0; row < N ; row++)
                 {
                     for (col = 0; col < M ; col++)
                     {
                         if ((sqr(row-row0) + sqr(col-col0)) <= radsqr) printf("x");
                         else printf(".");
                     }
                     printf("\r\n");
                 }
                 printf("%d\r\n\r\n",lastborder);
                 }

             }
         }
         result.add(&bordermin,1);
         //result.add(temp,input.readArray(temp));
     }
     input.close();

     output.open2write("output.txt");
     output.writeResult(result,testcases);     
     output.close();
     
     printf("READY!");
     
     char c;
     scanf("%c",&c);
     
     return -1;
}
