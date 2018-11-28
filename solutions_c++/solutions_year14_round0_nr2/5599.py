#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

class StringArray
{
    char** strings;
    int    numElem;
    int    allocated;
    
    public:
           
    StringArray()
    {
        numElem = 0;
        strings = new char*[50];
        allocated = 50;
    }
    
    bool add(char* str)      
    {
        int i;
        if (numElem == allocated)
        {
            char** stringsNew = new char*[allocated+50];
            if (stringsNew == NULL)
            {
                printf("BAJ VAN");
                return false;
            }
            for (i=0; i<allocated; i++)
            {
                stringsNew[i] = strings[i];
            } 
            allocated = allocated + 50;
            delete[] strings;
            strings = stringsNew;
            //printf("%d %s | ",allocated,strings[0]);
        }
        strings[numElem] = new char[strlen(str)+1];
        for (i=0; i<strlen(str)+1; i++)
        {
            strings[numElem][i] = str[i];
        }
        printf("added: %s\r\n",strings[numElem]);
        numElem++;
        return true;
    }
    
    char* get(int i)
    {
        return strings[i];      
    }
    
    int find(char* str)
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
        
        numElem = 0;
        strings = new char*[50];
        allocated = 50;
    }
    
    ~StringArray()
    {
        int i;
        for (i = 0; i<numElem; i++)
        {
            delete[] strings[i];
        }    
        delete[] strings;
    }
};

template <class T>
class Array2D
{
    T**    strings;
    int    numElem;
    int    allocated;
    
    public:
           
    Array2D()
    {
        numElem = 0;
        strings = new T*[50];
        allocated = 50;
    }
    
    bool add(T* str,int len)      
    {
        int i;
        if (numElem == allocated)
        {
            T** stringsNew = new T*[allocated+50];
            if (stringsNew == NULL)
            {
                printf("BAJ VAN");
                return false;
            }
            for (i=0; i<allocated; i++)
            {
                stringsNew[i] = strings[i];
            } 
            allocated = allocated + 50;
            delete[] strings;
            strings = stringsNew;
            //printf("%d %s | ",allocated,strings[0]);
        }
        strings[numElem] = new T[len];
        for (i=0; i<len; i++)
        {
            strings[numElem][i] = str[i];
        }
        printf("added: %d\r\n",strings[numElem][0]);
        numElem++;
        return true;
    }
    
    T* get(int i)
    {
        return strings[i];      
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
        
        numElem = 0;
        strings = new T*[50];
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
    }
};

class FileManager
{
    char* filename;
    FILE* f;
    
    int L,D;
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
        char c;
        int num = 0;
        array[0] = 0;
        bool neg = false;
        bool numread = false;

        array[num] = 0;
        
        while ((c = fgetc(f)) != '\r' && c != '\n' && c != EOF)
        {
            if (c >= '0' && c <= '9')
            {
                array[num] = array[num]*10 + c - '0';
                numread = true;
            }
            else if (c == '-')
            {
                neg = true;
                numread = false;
            }
            else
            {
                if (numread)
                {
                   if (neg) array[num] = -array[num];
                   num++;
                   array[num] = 0;
                }
                numread = false;
                neg = false;
            }
        }
        if (numread)
        {
           if (neg) array[num] = -array[num];
           num++;
           array[num] = 0;
        }
				        
        return num;
    }
    
    int readArray(double* array)
    {
    	//fscanf(f,"%f %f %f",&array[0],&array[1],&array[2]);
    	fscanf(f,"%lf",&(array[0]));
    	fscanf(f,"%lf",&(array[1]));
    	fscanf(f,"%lf",&(array[2]));
    	return 3;
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

    bool writeResult(StringArray& result,int n)
    {
         for (int i=0; i<n; i++)
         {
             fprintf(f,"Case #%d: %s\n",i+1,result.get(i));    
         }
    }     
};

void readCookie(FileManager& input,int* header, Array2D<double>& dataset, int& testcases)
{
     double temp[500];

 	 if (!input.open2read("B-large.in")) printf("error at file opening!");
     input.readArray(header);
     testcases = header[0];
     for (int i=0; i<testcases; i++)
     {
     	 //fscanf(input.getPointer(),"%f %f %f",&temp[0],&temp[1],&temp[2]);
     	 input.readArray(temp);
     	 printf(":%f %f %f\r\n",temp[0],temp[1],temp[2]);
         dataset.add(temp,3);
     }
     input.close();
}

void cookie(int* params, Array2D<double>& dataset, StringArray& result)
{
	double C,F,X;
	double *temp;
	int   i,i2;
	double last,time,sum=0;
	char  str[50];
	
	for (i = 0; i < params[0] ; i++)
	{
		temp = dataset.get(i);
		C = temp[0];
		F = temp[1];
		X = temp[2];
		//printf("-%f-%f-%f-\r\n",C,F,X);
		sum = 0;
		for (i2=0; 1; i2++)
		{
			time = sum + X / ( 2 + i2*F);
			if (i2 > 0 && time > last)
			{
				sprintf(str,"%.7f",last);
				result.add(str);
				break;
			}
			last = time;
			sum += C / ( 2 + i2*F);
		}
	}
}

void writeCookie(FileManager& output, StringArray& result, int testcases)
{
     output.open2write("cookie.out");
     output.writeResult(result,testcases);     
     output.close();
}

int main()
{
     FileManager input,output;
     int header[4];
     Array2D<double> dataset;
     int testcases;
     StringArray result;
     
     printf("START");
     
     readCookie(input,header,dataset,testcases);

     cookie(header,dataset,result);
     
     writeCookie(output,result,testcases);
     
     printf("READY!");
     
     char c;
     scanf("%c",&c);
     
     return -1;
}
