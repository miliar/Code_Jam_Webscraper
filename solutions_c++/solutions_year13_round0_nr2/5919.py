#include <stdio.h>
#include <iostream>
#include <string>
//#define DEBUG 1
using namespace std;

int main( int argc, char * argv[]){

    FILE *fp;
    FILE *flog;
    FILE *results;
    fp = fopen("input.dat","r");
    flog = fopen("log.txt","w");
    results = fopen("results.txt","w");
    if(fp == NULL || flog == NULL || results == NULL){
        fprintf(stderr,"Error opening input.dat\n");
        return(1);
    }  
    int cases = 0;
    fscanf(fp,"%d\n",&cases);
    fprintf(flog,"# of Cases %d\n",cases);

    for(int i = 0; i < cases; i ++){
        while(1){//makes sure we solve a case, requires a break to continue to next series        
            fprintf(flog,"Case %d\n\n",i+1);        
            int N,M;
            int smallest = 100;
            fscanf(fp,"%d %d\n",&N,&M);
            fprintf(flog,"N: %d M: %d \n",N,M);
            int grid[N][M];
            int valid = 1;
            for(int j = 0; j < N; j ++){
                for(int k = 0; k < M; k++){
                    fscanf(fp,"%d",&grid[j][k]);   
                    if(grid[j][k] < smallest)
                        smallest = grid[j][k];
                }
            }        
            fprintf(flog,"Smallest Element is %d\n",smallest);
            for(int j = 0; j < N; j ++){
                for(int k = 0; k < M; k++){
                    fprintf(flog,"%d ",grid[j][k]);
                }
                fprintf(flog,"\n");
            }        
            
            if(N ==1 || M == 1){
            
                fprintf(results,"Case #%d: YES\n",i+1);
                #ifdef DEBUG
                    fprintf(results,"N:%d M:%d\n",N,M);
                #endif
                valid = 0;
                break;
            }
            //1 is smallest 100 is biggest
            //fist lets check the border of the grid, if the smallest border element is larger than anything in the middle it is NOt possible
            int smallestBorderElement = 100;
            for(int j = 0; j < M; j ++){
                if(grid[0][j] < smallestBorderElement)
                    smallestBorderElement = grid[0][j];
            }
            for(int j = 0; j < M; j ++){
                if(grid[N-1][j] < smallestBorderElement)
                    smallestBorderElement = grid[N-1][j];
            }
            for(int j = 0; j < N; j ++){
                if(grid[j][0] < smallestBorderElement)
                    smallestBorderElement = grid[j][0];
            }
            for(int j = 0; j < N; j ++){
                if(grid[j][M-1] < smallestBorderElement)
                    smallestBorderElement = grid[j][M-1];
            }
            fprintf(flog,"Smallest border element is %d\n",smallestBorderElement);
            for(int j = 1; j < (N-1) && valid == 1; j++){
                for(int k = 1; k < (M-1) && valid == 1; k++){
                       fprintf(flog,"J: %d K: %d Grid[j][k]: %d\n",j,k,grid[j][k]);
                       if(grid[j][k] < smallestBorderElement) {                   
                            fprintf(results,"Case #%d: NO\n",i+1);
                            #ifdef DEBUG
                                fprintf(results,"N:%d M:%d\n",N,M);
                            #endif
                            valid = 0;
                            break;
                        }
                }
            }
            /*
           fprintf(flog,"Checking Left Down\n");
           for(int j = 0; j < N && valid == 1; j ++){
                if(grid[j][0] == smallest){
                    int y = 1;
                    int z = 1;
                    for(int k = 0; k < N; k ++){
                        fprintf(flog,"j: %d k: %d grid[k][0]:%d\n",j,k,grid[k][0]);       
                        if(grid[k][0] != smallest){
                            y = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }                        
                    }
                    for(int k = 0; k < M; k++){
                        fprintf(flog,"j: %d k: %d grid[j][k]:%d\n",j,k,grid[j][k]);                        
                        if(grid[j][k] != smallest){
                             z = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }              
                    }
                    if(!(y || z)){
                        fprintf(results,"Case #%d: NO\n",i+1);
                         #ifdef DEBUG
                                fprintf(results,"N:%d M:%d\n",N,M);
                         #endif
                        valid = 0;
                    }
                }
            }

          */
           for(int j = 0; j < N && valid == 1; j ++){
                for(int k = 0; k < M  && valid == 1;k++){
                    if(grid[j][k] == smallest){
                         int c1 = 1;
                         int c2 = 1;
                        for(int x = 0; x < N; x ++){
                            if(grid[x][k] != smallest){
                                c1 = 0;
                                break;
                            }
                        }
                        for(int x = 0; x < M; x ++){
                            if(grid[j][x] != smallest){
                                c2 = 0;
                                break;
                            }
                       }
                        if(!(c1 || c2)){

                            fprintf(results,"Case #%d: NO\n",i+1);
                            valid = 0;
                        }
                    }               
                }
           }/*
           fprintf(flog,"Checking Right Down\n");
           for(int j = 0; j < N && valid == 1; j ++){
                if(grid[j][M-1] == smallest){
                    int y = 1;
                    int z = 1;
                    for(int k = 0; k < N; k ++){
                        fprintf(flog,"j: %d k: %d grid[k][M-1]:%d\n",j,k,grid[k][M-1]);       
                        if(grid[k][M-1] != smallest){
                            y = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }                        
                    }
                    for(int k = 0; k < M; k++){
                        fprintf(flog,"j: %d k: %d grid[j][k]:%d\n",j,k,grid[j][k]);                        
                        if(grid[j][k] != smallest){
                             z = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }              
                    }
                    if(!(y || z)){
                        fprintf(results,"Case #%d: NO\n",i+1);
                         #ifdef DEBUG
                                fprintf(results,"N:%d M:%d\n",N,M);
                         #endif
                        valid = 0;
                    }
                }
            }



           fprintf(flog,"Checking Top Across\n");
           for(int j = 0; j < M && valid == 1; j ++){
                if(grid[0][j] == smallest){
                    int y = 1;
                    int z = 1;
                    for(int k = 0; k < M; k ++){
                        fprintf(flog,"j: %d k: %d grid[0][k]:%d\n",j,k,grid[0][k]);       
                        if(grid[0][k] != smallest){
                            y = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }                        
                    }
                    for(int k = 0; k < N; k++){
                        fprintf(flog,"j: %d k: %d grid[k][j]:%d\n",j,k,grid[k][j]);                        
                        if(grid[k][j] != smallest){
                             z = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }              
                    }
                    if(!(y || z)){
                        fprintf(results,"Case #%d: NO\n",i+1);
                         #ifdef DEBUG
                                fprintf(results,"N:%d M:%d\n",N,M);
                         #endif
                        valid = 0;
                    }
                }
            }
           fprintf(flog,"Checking Bottom Across\n");
           for(int j = 0; j < M && valid == 1; j ++){
                if(grid[N-1][j] == smallest){
                    int y = 1;
                    int z = 1;
                    for(int k = 0; k < M; k ++){
                        fprintf(flog,"j: %d k: %d grid[N-1][k]:%d\n",j,k,grid[N-1][k]);       
                        if(grid[N-1][k] != smallest){
                            y = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }                        
                    }
                    for(int k = 0; k < N; k++){
                        fprintf(flog,"j: %d k: %d grid[k][j]:%d\n",j,k,grid[k][j]);                        
                        if(grid[k][j] != smallest){
                             z = 0;
                            fprintf(flog,"Row NOt The Valid Path\n");
                            break;
                        }              
                    }
                    if(!(y || z)){
                        fprintf(results,"Case #%d: NO\n",i+1);
                         #ifdef DEBUG
                                fprintf(results,"N:%d M:%d\n",N,M);
                         #endif
                        valid = 0;
                    }
                }
            }*/
            //default case - YES 
            if(valid == 1){
                fprintf(results,"Case #%d: YES\n",i+1);
                 #ifdef DEBUG
                    fprintf(results,"N:%d M:%d\n",N,M);
                 #endif
            }
            break;
        }
    }
    fclose(fp);
    fclose(flog);
    fclose(results);
}
