#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

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
     Array2D<int>    dataset_num;
     //Array2D<long>   dataset;
     //Array2D<double> dataset;
     StringArray     dataset;
     StringArray     dataset_filt;
     int testcases;
     //Array2D<int>    result;
     //Array2D<long>   result;
     //Array2D<double> result;
     StringArray     result;
     
     
     printf("START");
     
     int tmpint[120];
     char tmpstr[120];
     char tmpstr2[120];
     double avg[120];
     int avgint[120];
     char *str,*str2;
     int* nums;
     int N,i2,len,i3,num,lastlen,move;
     bool ok;

 	 if (!input.open2read("input.txt")) printf("error at file opening!");
     input.readArray(header);
     testcases = header[0];
     for (int i=0; i<testcases; i++)
     {
         input.readNum(&N); input.readString(tmpstr,120);
         ok = true;
         for (i2=0; i2<120; i2++)
         {
             avg[i2] = 0;
         }
         for (i2=0; i2<N; i2++)
         {
             input.readString(tmpstr,120);  //printf("str: %s\r\n",tmpstr);
             dataset.add(tmpstr);
             //result.add(temp,input.readArray(temp));

             tmpstr2[0] = tmpstr[0];
             lastlen = len;
             len = 0;
             num = 1;
             
             for (i3 = 1; i3<strlen(tmpstr)+1; i3++)
             {
                 if (tmpstr[i3] != tmpstr[i3-1])
                 {
                     tmpstr2[len+1] = tmpstr[i3];
                     tmpint[len] = num;
                     avg[len] += num;
                     num = 1;
                     len++;
                 }
                 else
                 {
                     num++;    
                 }
             }
             //printf("%s\r\n",tmpstr2);
             dataset_filt.add(tmpstr2);
             dataset_num.add(tmpint,len);
             
             if (i2 > 0 && len!=lastlen)
             {
                    printf("len: %d -> %d\r\n",lastlen,len);
                    ok = false;
                    break;
             }
         }

         for (i2=0; i2<120; i2++)
         {
             avg[i2] = avg[i2]/N;
             avgint[i2] = (int)round(avg[i2]);
         }
         
         if (ok)
         {
             str = dataset_filt.get(0);
             for (i2 = 1; i2<N ; i2++)
             {
                 str2 = dataset_filt.get(i2);
                 if (strcmp(str,str2)) 
                 {
                    printf("%s <> %s\r\n",str,str2);
                    ok = false; break; 
                 }    
             }
         }

         if (!ok)
         {         
             result.add("Fegla Won");
             dataset.clear();
             dataset_filt.clear();
             dataset_num.clear();
             continue;
         }

         move = 0;
      
         for (i2 = 0; i2<N ; i2++)
         {
             nums = dataset_num.get(i2);
             for (i3 = 0; i3<len ; i3++)
             {
                 move += abs(nums[i3]-avgint[i3]);
             }
         }

         sprintf(tmpstr,"%d",move);

         result.add(tmpstr);
         
         dataset.clear();
         dataset_filt.clear();
         dataset_num.clear();
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
