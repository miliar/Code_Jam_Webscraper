void CDlgGoogleCodeJam::QR2014ProblemB(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, j, k, T;
	double			dCost, dBonus, dGoal, dProduction, dCount;
	bool			bResult, bTest;
	CString			sReadText, sWriteText, sTempText, str;

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	T = atoi(sReadText);
	for (i = 1; i <= T; i++)
	{
		pInputFile->ReadString(sReadText);
		sscanf_s(sReadText,"%lf %lf %lf", &dCost, &dBonus, &dGoal);

		// Do the job

		bResult = true;
		bTest = true;
		dCount = 0;
		dProduction = 2;

		while (dCount < dGoal)
		{
			if (dGoal/dProduction > (dCost/dProduction + dGoal/(dProduction+dBonus)))
			{
				dCount += dCost/dProduction;
				dProduction += dBonus;
			}
			else
			{
				dCount += dGoal/dProduction;
				break;
			}
						
		}
		
		sTempText.Format("%.7lf", dCount);

		// Print result
		sWriteText.Format("Case #%d: %s\n", i, sTempText);
		pOutputFile->WriteString(sWriteText);
	}
}
