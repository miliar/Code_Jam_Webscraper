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

class IntArray2D
{
    int**  strings;
    int    numElem;
    int    allocated;
    
    public:
           
    IntArray2D()
    {
        numElem = 0;
        strings = new int*[50];
        allocated = 50;
    }
    
    bool add(int* str,int len)      
    {
        int i;
        if (numElem == allocated)
        {
            int** stringsNew = new int*[allocated+50];
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
        strings[numElem] = new int[len];
        for (i=0; i<len; i++)
        {
            strings[numElem][i] = str[i];
        }
        printf("added: %d\r\n",strings[numElem][0]);
        numElem++;
        return true;
    }
    
    int* get(int i)
    {
        return strings[i];      
    }
    
    int find(int* str)
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
        strings = new int*[50];
        allocated = 50;
    }
    
    ~IntArray2D()
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

    bool writeStringResult(StringArray& result,int n)
    {
         for (int i=0; i<n; i++)
         {
             fprintf(f,"Case #%d: %s\n",i+1,result.get(i));    
         }
    }     
};

void readTrick(FileManager& input,int* header, IntArray2D& dataset, int& testcases)
{
     int temp[500];
     int len;

 	 if (!input.open2read("A-small-attempt0.in")) printf("error at file opening!");
     input.readArray(header);
     testcases = header[0];
     for (int i=0; i<(testcases*10); i++)
     {
     	 len = input.readArray(temp);
     	 printf("-%d-",len);
         dataset.add(temp,len);
     }
     input.close();
}

void trick(int* params, IntArray2D& dataset, StringArray& result)
{
	int i,i2,i3;
	int rownum1,rownum2;
	int *row1, *row2;
	int found;
	int number;
	char str[10];
	
	for (i = 0; i < params[0] ; i++ )
	{
		found   = 0;
		number  = 0;
		rownum1 = *(dataset.get(i*10));
		rownum2 = *(dataset.get(i*10+5));
		row1    = dataset.get(i*10+rownum1);
		row2    = dataset.get(i*10+5+rownum2);
		for (i2 = 0; i2<4; i2++)
		{
		    for (i3 = 0; i3<4 ; i3++)
		    {
		    	if (row1[i2]==row2[i3]) 
		    	{
					found++;
		    		number = row1[i2];
				}
		    }
		}
		if (found == 0)
		{
			result.add("Volunteer cheated!");
		}
		if (found > 1)
		{
			result.add("Bad magician!");
		}
		if (found == 1)
		{
		    itoa(number,str,10);
			result.add(str);
		}
	}
}

void writeTrick(FileManager& output, StringArray& result, int testcases)
{
     output.open2write("trick.out");
     output.writeStringResult(result,testcases);     
     output.close();
}

int main()
{
     FileManager input,output;
     int header[4];
     IntArray2D dataset;
     int testcases;
     StringArray result;
     
     printf("START");
     
     readTrick(input,header,dataset,testcases);

     trick(header,dataset,result);
     
     writeTrick(output,result,testcases);
     
     printf("READY!");
     
     char c;
     scanf("%c",&c);
     
     return -1;
}
